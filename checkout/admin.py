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
                    'grand_total', 'original_basket', 'stripe_pid')
    
    fields = ('order_number', 'full_name', 'email', 'phone_number', 
            'country', 'postcode', 'town_or_city', 'street_address1', 
            'street_address2', 'county', 'date', 'delivery_cost', 
            'order_total', 'grand_total', 'delivery_option', 'original_basket', 'stripe_pid')
    
    list_display = ('order_number', 'date', 'full_name', 'grand_total', 'delivery_option', )

    ordering = ('-date',)

# class DeliveryOrderAdmin(admin.ModelAdmin):
#     readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'grand_total', 'delivery_address',)
#     fields = ('order_number', 'full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county', 'date', 'delivery_cost', 'order_total', 'grand_total', 'delivery_address',)
#     list_display = ('order_number', 'date', 'full_name', 'grand_total',)
#     ordering = ('-date',)

# class CollectionOrderAdmin(admin.ModelAdmin):
#     readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'grand_total',)
#     fields = ('order_number', 'full_name', 'email', 'phone_number', 'date', 'delivery_cost', 'order_total', 'grand_total',)
#     list_display = ('order_number', 'date', 'full_name', 'grand_total',)
#     ordering = ('-date',)



admin.site.register(Order, OrderAdmin)
# admin.site.register(DeliveryOrder, DeliveryOrderAdmin)
# admin.site.register(CollectionOrder, CollectionOrderAdmin)
