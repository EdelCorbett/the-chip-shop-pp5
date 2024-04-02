from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

# Create your views here.

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def delete_profile(request):
    """ Delete the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = request.user
    profile.delete()
    user.delete()
    logout(request)
    messages.success(request, 'Profile deleted successfully')
    return HttpResponseRedirect(reverse('home'))

    # return render(request, 'home/index.html')
