from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reviews
from menu.models import Menuitem
from .forms import ReviewForm
# Create your views here.
def add_review(request, menuitem_id):
    menuitem = get_object_or_404(Menuitem, pk=menuitem_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.menuitem = menuitem
            review.user = request.user
            review.save()
            return render(request, 'menu/menuitem_detail.html', {'menuitem': menuitem})
    else:
        form = ReviewForm()
    return render(request, 'review/add_review.html', {'form': form, 'menuitem': menuitem})



@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id)
    review.delete()
    return render(request, 'delete_review.html')

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'form': form})
