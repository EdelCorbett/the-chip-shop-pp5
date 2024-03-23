from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Menuitem

def delivery_info(request):

    return {'STANDARD_DELIVERY_PRICE': settings.STANDARD_DELIVERY_PRICE}

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0

    basket = request.session.get('basket', {})
    print(basket)

    

    # for item_id, quantity in basket.items():
    #     menu = get_object_or_404(Menuitem, pk=item_id)
    #     total += quantity * menu.price
    #     product_count += quantity
    #     basket_items.append({
    #         'item_id': item_id,
    #         'quantity': quantity,
    #         'menu': menu,
    #     })
    
    for item_id, item_data in basket.items():
        menu_item = get_object_or_404(Menuitem, pk=item_id)
        print(f"item_data: {item_data}, menu_item.price: {menu_item.price}")
        total += item_data * menu_item.price
        product_count += item_data
        basket_items.append({
            'menu_item': menu_item,
            'item_id': item_id,
            'quantity': item_data,
            
        })
    # Check if delivery option is selected and adjust delivery charge accordingly
    delivery_option = request.session.get('delivery_option', 'collection')
    if total < settings.FREE_DELIVERY_THRESHOLD:
        if delivery_option == 'delivery':
            delivery = Decimal(settings.STANDARD_DELIVERY_PRICE)
        else:
            delivery = 0
    else:
        delivery = 0

    # Calculate grand total including delivery charge
    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    print(grand_total)
    print(delivery)
    print(total)

    return context



