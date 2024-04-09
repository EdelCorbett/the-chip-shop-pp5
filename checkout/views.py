from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import BaseOrderForm, DeliveryOptionForm
from basket.contexts import basket_contents
from menu.models import Menuitem
from .models import Order, OrderLineItem
from profiles.forms import UserProfileForm
from profiles.models import UserProfile


import stripe
import json   

# Create your views here.
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get delivery option from session
        delivery_option = request.session.get('delivery_option')

        # Calculate delivery charge based on delivery option
        if delivery_option == 'delivery':
            delivery = Decimal(settings.STANDARD_DELIVERY_PRICE)
        else:
            delivery = 0

        # Retrieve the existing PaymentIntent
        payment_intent = stripe.PaymentIntent.retrieve(pid)

        # Add delivery charge to the total amount
        new_amount = int(payment_intent.amount + delivery * 100)

        # Update the PaymentIntent with the new amount and metadata
        stripe.PaymentIntent.modify(pid, amount=new_amount, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'username': request.user,
            # 'delivery_option': delivery_option,
        })

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def delivery_option(request):
    if request.method == 'POST':
        order_number = request.POST.get('order_number')
        if order_number:
            order = Order.objects.get(order_number=order_number)
            delivery_option_form = DeliveryOptionForm(request.POST,instance=order)
        else:
            delivery_option_form = DeliveryOptionForm(request.POST)
       
        if delivery_option_form.is_valid():
            delivery_option = delivery_option_form.cleaned_data['delivery_option']
            request.session['delivery_option'] = delivery_option
            print(request.session['delivery_option'])
            return redirect(reverse('checkout'))
        else:
            messages.error(request, 'There was an error with your form.')
            return redirect(reverse('delivery_option'))
    else:
        delivery_option_form = DeliveryOptionForm()
        template = 'checkout/delivery_option.html'
        context = {
            'delivery_option_form': delivery_option_form,
        }
        return render(request, template, context)       



def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    delivery_option = request.session.get('delivery_option')
    print(delivery_option)
    if not delivery_option:
        messages.error(request, 'Please select a delivery option.')
        print("Please select a delivery option.")
        return redirect(reverse('delivery_option'))
    
   
    if request.method == 'POST':
       
        basket = request.session.get('basket', {})
        print(basket)

        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'street_address1': request.POST.get('street_address1'),
            'street_address2': request.POST.get('street_address2'),
            'town_or_city': request.POST.get('town_or_city'),
            'postcode': request.POST.get('postcode'),
            'country': request.POST.get('country'),
            'delivery_option': delivery_option,
            'payment_method': request.POST.get('payment_method'),
            
            
        }

        
        
        order_form = BaseOrderForm(form_data, delivery_option=delivery_option)
        print(order_form)


        if order_form.is_valid():  
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.delivery_option = delivery_option
            order.delivery = Decimal(settings.STANDARD_DELIVERY_PRICE)#
            print("delivery option", order.delivery_option)
            order.save()   
            print(order.delivery)
            
            for item_id, quantity in basket.items():
                try:
                    menu = Menuitem.objects.get(pk=item_id)
                    
                    order_line_item = OrderLineItem(
                        order=order,
                        menuitem=menu,
                        quantity=quantity
                    )
                    order_line_item.save()
                    print("order_line_item_save", order_line_item)            
                    
                except Menuitem.DoesNotExist:
                        messages.error(request, (
                            "One of the menu items in your basket wasn't found in our database. "
                            "Please call us for assistance!")
                        )
                        order.delete()

                        return redirect(reverse('view_basket'))
                
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        
        else:
            print(order_form.errors)
            messages.error(request, 'There was an error with your form can you  Please double check your information.')
            return redirect(reverse('checkout'))
                

    else:
        print("Retrieving basket from session..."),
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse('menu'))
        
        current_basket = basket_contents(request)
        print("Calculating total...")
        total = current_basket['total']

        DELIVERY_MINIMUM_ORDER_SPEND = 10  
        if delivery_option == 'delivery' and total < DELIVERY_MINIMUM_ORDER_SPEND:
            messages.error(request, f"Your order must be at least €{DELIVERY_MINIMUM_ORDER_SPEND} for delivery.")
            return redirect(reverse('delivery_option'))

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = BaseOrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = BaseOrderForm(delivery_option=delivery_option)
        else:
            order_form = BaseOrderForm(delivery_option=delivery_option)
            print(delivery_option)
        

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')
            
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'delivery_option': delivery_option,
            
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    basket = basket_contents(request)
    delivery = basket['delivery']
    print(delivery)

    order_total = sum(item['menu_item'].price * item['quantity'] for item in basket['basket_items'])
    print(order_total)
    grand_total = order_total + delivery
    print("grand_total",grand_total)
    print(delivery)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save() # check here!!!!!!!!!!!!!!!!!!!
        print( "profile save",order.user_profile)
        order_url = request.build_absolute_uri(reverse('view_orders', args=[order_number]))
        print("Order URL:", order_url)
        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                messages.success(request, f'Order successfully processed! \
                    Your order number is {order_number}. A confirmation \
                    email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_total': order_total,
        'delivery': delivery,
        'grand_total': grand_total,

    }

    return render(request, template, context)


def view_orders(request, order_number=None):
    if order_number is not None:
        orders = [get_object_or_404(Order, order_number=order_number)]
        template = 'checkout/view_orders.html'
    else:
        orders = Order.objects.all()
        template = 'checkout/view_orders.html'

    context = {
        'orders': orders,
    }

    return render(request, template, context)