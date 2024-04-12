from django.urls import path
from . import views
from .views import view_orders
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('delivery_option/', views.delivery_option, name='delivery_option'),
    path('checkout_success/<order_number>',
        views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/',
        views.cache_checkout_data, name='cache_checkout_data'),
    path('view_orders/', views.view_orders, name='view_orders_no_arg'),
    path('view_orders/<str:order_number>/',
        views.view_orders, name='view_orders'),
    path('wh/', webhook, name='webhook'),
]
