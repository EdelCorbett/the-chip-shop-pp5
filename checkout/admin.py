from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem

    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdmin,)
    readonly_fields = ('order_number', 'date',
                       'original_basket', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'full_name', 'email',
              'phone_number',
              'country', 'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'date', 'delivery',
              'order_total', 'grand_total', 'delivery_option',
              'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'grand_total', 'delivery_option',
                    'delivery', 'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
