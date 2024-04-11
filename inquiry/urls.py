from django.urls import path
from . import views


urlpatterns = [
    path('inquiry/', views.inquiry_form, name='inquiry_form'),
    path('inquiry_success/', views.inquiry_success, name='inquiry_success'),
]
