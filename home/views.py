from django.shortcuts import render
from menu.models import Favorite
# Create your views here.
def index(request):
    """ A view to return the index page """
    favorites = Favorite.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'home/index.html', {'favorites': favorites})
