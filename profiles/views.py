from django.shortcuts import render

# Create your views here.
def profile(request):
    """ Display the user's profile. """
    
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }
    
    return render(request, template, context)