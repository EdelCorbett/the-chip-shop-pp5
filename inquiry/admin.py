from django.contrib import admin

# Register your models here.
from .models import Inquiry

class InquiryAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone', 'created_at', 'contacted')
    list_editable = ('contacted',)

admin.site.register(Inquiry, InquiryAdmin)