from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from menu.models import Menuitem
from django.http import HttpResponse
from .contexts import basket_contents

# Create your views here.

def view_basket(request):
    """ A view to return the basket page """
    basket = request.session.get('basket', {})
    total = 0
    for item_id, quantity in basket.items():
        menu = Menuitem.objects.get(pk=item_id)
        total += menu.price * quantity
    return render(request, 'basket.html', {'total': total})

def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    menu = Menuitem.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if redirect_url is None:
        redirect_url = reverse('home')

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {menu.name} quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {menu.name} to your basket')

    request.session['basket'] = basket
    
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """
    
    menu = Menuitem.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {menu.name} quantity to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {menu.name} from your basket')
        

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

def remove_from_basket(request, item_id):
    """ Decrease the quantity of the specified item in the shopping basket """

    try:
        menu = Menuitem.objects.get(pk=item_id)
        basket = request.session.get('basket', {})

        if item_id in basket:
            if basket[item_id] > 1:
                # Decrease the quantity of the item
                basket[item_id] -= 1
                messages.success(request, f'Removed {menu.name} from your basket')
            else:
                # If the quantity is 1, remove the item entirely
                basket.pop(item_id)
                messages.success(request, f'Removed {menu.name} from your basket')

            request.session['basket'] = basket
            return HttpResponse('status: 200')
        else:
            messages.error(request, 'Error: Item not found in your basket')
            return HttpResponse(status=500)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)