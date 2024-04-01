from django import forms
from .models import Order, OrderLineItem


class BaseOrderForm(forms.ModelForm):
   

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                'street_address1', 'street_address2',
                'town_or_city', 'postcode', 'country',
                'county', )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        delivery_option = kwargs.pop('delivery_option','default')
        print(delivery_option)
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
            'delivery_option': 'Delivery Option',
            
        }

        if delivery_option == 'collection':
            print('delivery_option is collection')
            for field in ['phone_number', 'street_address1', 'street_address2', 'town_or_city', 'country']:
                self.fields[field].required = False

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
    print('DeliveryOptionForm')
    delivery_option = forms.ChoiceField(choices=DELIVERY_OPTIONS, required=True)





    

