from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the Contact model.
    """
    list_display = [
        'full_name',
        'email',
        'enquiry_subject',
        'order_number',
        'body',
        'dimensions',
        'image_url',
        'image',
        'order_number',
        'date',
    ]


admin.site.register(Contact, ContactAdmin)
