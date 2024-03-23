from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('delivery_option/', views.delivery_option, name='delivery_option'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),


]