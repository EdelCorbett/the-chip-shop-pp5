from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    
    readonly_fields = ('lineitem_total',)



class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdmin,)
    readonly_fields = ('order_number', 'date', 
                    'delivery_cost', 'order_total',
                    'grand_total',)
    
    feilds = ('order_number', 'full_name', 'email', 'phone_number', 
            'country', 'postcode', 'town_or_city', 'street_address1', 
            'street_address2', 'county', 'date', 'is_delivery','delivery_cost', 
            'order_total', 'grand_total',)
    
    list_display = ('order_number', 'date', 'full_name','is_delivery', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
