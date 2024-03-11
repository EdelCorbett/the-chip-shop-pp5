from django.shortcuts import render
from .models import menuitem

# Create your views here.
def all_menu(request):
    """ A view to return the index page """

    menu = menuitem.objects.all()

    context = {
        'menu': menu,
    }

    return render(request, 'menu/menu.html', context)
