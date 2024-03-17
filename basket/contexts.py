from decimal import Decimal
from django.conf import settings

def delivery_info(request):
    return {'STANDARD_DELIVERY_PRICE': settings.STANDARD_DELIVERY_PRICE}

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PRICE)
    

    # # Check if delivery option is selected and adjust delivery charge accordingly
    # if 'delivery' in request.session and request.session['delivery'] == 'delivery':
    #     delivery = Decimal(settings.STANDARD_DELIVERY_PRICE)

    # Calculate grand total including delivery charge
    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context



