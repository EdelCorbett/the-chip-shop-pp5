from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


# Create your views here.
def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('menu'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OduTqBJWoE0Jlvsmm5hum7Lpqz07TKZhi4LC6DJ0HjurE6bsGF1exEbBdSEFIAFfaHMkKzB9YqwN8uzo4RWdmCv00YNRLBThr',
        'client_secret': 'test client secret', 
    }

    return render(request, template, context)