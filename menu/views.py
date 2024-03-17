from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Menuitem

# Create your views here.

def all_menu(request):
    """ A view to return menu page"""

    menu = Menuitem.objects.all()
    category = Category.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                menu = menu.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            menu = menu.order_by(sortkey)


        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            menu = menu.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('menu'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            menu = menu.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'menu': menu,
        'search_term': query,
        'categories': category,
        'current_categories': category,
        'current_sorting': current_sorting,
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
