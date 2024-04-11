from django.contrib import admin
from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):

    list_display = ('user', 'menuitem', 'rating', 'created_on', 'comment')
    list_filter = ('menuitem', 'rating')


admin.site.register(Reviews, ReviewsAdmin)


