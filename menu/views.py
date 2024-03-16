from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Category, Menuitem

# Create your views here.

def all_menu(request):
    """ A view to return menu page"""

    menu = Menuitem.objects.all()
    categories = Category.objects.all() 
    

    context = {
        'menu': menu,
        'categories': categories,
        'MEDIA_URL': settings.MEDIA_URL,

        
    }

    return render(request, 'menu/menu.html', context)

def menu_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    menuitems = Menuitem.objects.filter(category=category)
    return render(request, 'menu/menu.html', {'menu': menuitems, 'categories': Category.objects.all()})


def menuitem_detail(request, menuitem_id):
    """ A view to return individual menu items information"""
    menuitem = get_object_or_404(Menuitem, pk=menuitem_id)
    
    context = {
        'menuitem': menuitem,   
    }

    return render(request, 'menu/menuitem_detail.html', context)
