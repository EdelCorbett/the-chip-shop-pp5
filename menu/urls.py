from django.contrib import admin
from django.urls import path 
from . import views


urlpatterns = [
    path('',views.all_menu,name='menu'),
    path('menu/<int:menuitem_id>/', views.menuitem_detail, name='menuitem_detail'),
    path('menu/category/<int:category_id>/', views.menu_by_category, name='menu_by_category'),
    path('add/', views.add_menuitem, name='add_menuitem'),
    path('edit/<int:menuitem_id>/', views.edit_menuitem, name='edit_menuitem'),
    path('delete/<int:menuitem_id>/', views.delete_menuitem, name='delete_menuitem'),
]

