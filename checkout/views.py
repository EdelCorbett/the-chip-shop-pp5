from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import BaseOrderForm, DeliveryOptionForm
from basket.contexts import basket_contents
from menu.models import Menuitem
from .models import Order, OrderLineItem


import stripe
import json   

# Create your views here.
def delivery_option(request):
    if request.method == 'POST':
        delivery_option_form = DeliveryOptionForm(request.POST)
        if delivery_option_form.is_valid():
            delivery_option = delivery_option_form.cleaned_data['delivery_option']
            request.session['delivery_option'] = delivery_option
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
    if not delivery_option:
        messages.error(request, 'Please select a delivery option.')
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
            
            
        }

        form_data = request.POST.copy() 
        form_data['delivery_option'] = delivery_option 
        order_form = BaseOrderForm(form_data, delivery_option=delivery_option)
        print(order_form)

        

        if delivery_option == 'delivery':
            order_form.fields['street_address1'].required = True
            order_form.fields['town_or_city'].required = True
            order_form.fields['postcode'].required = True
            order_form.fields['country'].required = True
       

        if order_form.is_valid():  
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()   
            
            for item_id, quantity in basket.items():
                try:
                    menu = Menuitem.objects.get(pk=item_id)
                    
                    order_line_item = OrderLineItem(
                        order=order,
                        menuitem=menu,
                        quantity=quantity
                    )
                    order_line_item.save()
                    
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
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = BaseOrderForm(delivery_option=delivery_option)
        

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
    order = get_object_or_404(Order,order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
     
    
    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        
        
    }

    return render(request, template, context)