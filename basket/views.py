from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ A view to return the basket page """

    return render(request, 'basket.html')