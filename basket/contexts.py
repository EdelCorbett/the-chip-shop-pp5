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
    delivery = 0
    free_delivery_delta = 0
    grand_total = 0

    basket = request.session.get('basket', {})
    

    delivery_option = request.session.get('delivery_option')
    for item_id, item_data in basket.items():
        menu_item = get_object_or_404(Menuitem, pk=item_id)
        total += item_data * menu_item.price
        product_count += item_data
        basket_items.append({
            'menu_item': menu_item,
            'item_id': item_id,
            'quantity': item_data,
            'delivery_option': delivery_option,
            
        })
   # Check if delivery option is selected and adjust delivery charge accordingly
    
    print("delivery_option: ", delivery_option)
    if total < settings.FREE_DELIVERY_THRESHOLD:
        if delivery_option == 'delivery':
            delivery = Decimal(settings.STANDARD_DELIVERY_PRICE)
        else:
            delivery = 0
    # else:
    #     delivery = 0
    print("delivery: ", delivery)
    # Calculate grand total including delivery charge
    grand_total = total + delivery
    print("total: ", total)
    print("delivery: ", delivery)
    print("grand_total: ", grand_total)


    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery ,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'delivery_option': delivery_option,
        
    }

    return context



