from django.contrib import admin
from .models import Item, Category

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'price',
        'dimensions',
        'image',
        'how_many_in_stock'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
