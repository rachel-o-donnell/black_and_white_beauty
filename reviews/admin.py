from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'commission',
        'user',
        'title',
        'body',
        'date',
        'image',
        'featured',
    )

    ordering = ('-date',)


admin.site.register(Review, ReviewAdmin)
