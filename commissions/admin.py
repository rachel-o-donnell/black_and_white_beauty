from django.contrib import admin
from .models import Commissions


class CommissionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'dimensions',
        'image',
        'brief'
    )


admin.site.register(Commissions, CommissionsAdmin)
