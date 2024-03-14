from django.shortcuts import render
from .models import menuitem, Category

# Create your views here.
def all_menu(request):
    """ A view to return the index page """

    menu = menuitem.objects.all()
    categories = Category.objects.all() 
    

    context = {
        'menu': menu,
        'categories': categories,

        
    }

    return render(request, 'menu/menu.html', context)
