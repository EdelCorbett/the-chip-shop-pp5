import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from menu.models import Menuitem
from profiles.models import UserProfile
from decimal import Decimal
from django_countries.fields import CountryField

# Create your models here.
class Order(models.Model):

    DELIVERY_OPTIONS = [
        ('delivery', 'Delivery'),
        ('collection', 'Collection'),
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_option = models.CharField(max_length=10, null=False, blank=False, default='collection')
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

   
    

    

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        print(f"Order total: {self.order_total}")
        print(f"Delivery option: {self.delivery_option}")
        
        print ("delivery_option")
            
            # Check if delivery option is selected and order total is below the free delivery threshold
        if self.delivery_option == 'delivery' :
            self.delivery_cost = Decimal(settings.STANDARD_DELIVERY_PRICE)
            print(f"Delivery cost: {self.delivery_cost}")
            print("Delivery_option is delivery") 
        else:
            self.delivery_cost = 0
            print ("delivery cost")
            
            # Calculate grand total
        self.grand_total = self.order_total + self.delivery_cost
        print ("grand total")
        print(f"Grand total: {self.grand_total}")
        self.save()
        

    def save(self, *args, **kwargs):
            """
            Override the original save method to set the order number
            if it hasn't been set already.
            """
            if not self.order_number:
             self.order_number = self._generate_order_number()
            print(f"Saving order: delivery_option={self.delivery_option}, delivery_cost={self.delivery_cost}, grand_total={self.grand_total}")
            super().save(*args, **kwargs)

    def __str__(self):
        print(self.order_number)
        return self.order_number

    
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    menuitem = models.ForeignKey(Menuitem, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.menuitem.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order {self.order.order_number}'