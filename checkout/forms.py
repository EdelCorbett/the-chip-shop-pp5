from django import forms
from .models import Order, OrderLineItem


class BaseOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                'street_address1', 'street_address2',
                'town_or_city', 'postcode', 'country',
                'county')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            
        }
        if 'full_name' in self.fields:
            self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

class DeliveryOptionForm(forms.Form):
    DELIVERY_OPTIONS = [
        ('delivery', 'Delivery'),
        ('collection', 'Collection'),
    ]
    delivery_option = forms.ChoiceField(choices=DELIVERY_OPTIONS, required=True)

    


     

# from django import forms
# from .models import Order, DeliveryOrder, CollectionOrder


# class BaseOrderForm(forms.ModelForm):
#     delivery_option = forms.ChoiceField(choices=[('delivery', 'Delivery'), ('collection', 'Collection')])
#     class Meta:
#         model = Order
#         fields = ('full_name', 'email', 'phone_number',
#                 'street_address1', 'street_address2',
#                 'town_or_city','county', 'postcode', 'country')
#     def __init__(self, *args, **kwargs):
#         """
#         Add placeholders and classes, remove auto-generated
#         labels and set autofocus on first field
#         """
#         super().__init__(*args, **kwargs)
#         placeholders = {
#             'full_name': 'Full Name',
#             'email': 'Email Address',
#             'phone_number': 'Phone Number',
#             'postcode': 'Postal Code',
#             'town_or_city': 'Town or City',
#             'street_address1': 'Street Address 1',
#             'street_address2': 'Street Address 2',
#             'county': 'County, State or Locality',
#             'delivery_option': 'Delivery Option',
#         }
#         self.fields['full_name'].widget.attrs['autofocus'] = True
#         for field in self.fields:
#                 if field != 'country':
#                     if self.fields[field].required:
#                         placeholder = f'{placeholders[field]} *'
#                     else:
#                         placeholder = placeholders[field]
#                     self.fields[field].widget.attrs['placeholder'] = placeholder
#                 self.fields[field].widget.attrs['class'] = 'stripe-style-input'
#                 self.fields[field].label = False

        
#     def clean(self):
#         cleaned_data = super().clean()
#         delivery_option = cleaned_data.get('delivery_option')
#         order_total = self.instance.order_total
#         if delivery_option == 'delivery' and order_total < 10:
#             self.add_error('delivery_option', 'Delivery is not available for orders less than €10.')


# class DeliveryOrderForm(BaseOrderForm):
#     delivery_address = forms.CharField(max_length=255, required=True)

#     class Meta(BaseOrderForm.Meta):
#         model = DeliveryOrder
#         fields = BaseOrderForm.Meta.fields + ('delivery_address',)


# class CollectionOrderForm(BaseOrderForm):
#     collection_time = forms.DateTimeField(required=True)

#     class Meta(BaseOrderForm.Meta):
#         model = CollectionOrder
#         fields = BaseOrderForm.Meta.fields + ('collection_time',)


