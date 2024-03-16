from django.contrib import admin
from .models import Category, Menuitem



# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class MenuitemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Menuitem, MenuitemAdmin)
