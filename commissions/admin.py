from django.contrib import admin


class CommissionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'dimensions',
        'image',
        'brief'
    )
