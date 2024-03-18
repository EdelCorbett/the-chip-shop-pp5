from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from menu.models import Menuitem
from django.http import HttpResponse
from .contexts import basket_contents

# Create your views here.

def view_basket(request):
    """ A view to return the basket page """
    return render(request, 'basket.html')

def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    menu = Menuitem.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {menu.name} to your basket')

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

def remove_from_basket(request, item_id):
    """ Decrease the quantity of the specified item in the shopping basket """

    basket = request.session.get('basket', {})

    if item_id in basket:
        if basket[item_id] > 1:
            # Decrease the quantity of the item
            basket[item_id] -= 1
        else:
            # If the quantity is 1, remove the item entirely
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse('status: 200')
    else:
        return HttpResponse('status: 500')