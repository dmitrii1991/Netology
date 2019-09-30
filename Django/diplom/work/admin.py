from django.contrib import admin

from .models import Bd

class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'manufacturer', 'launch', 'description', 'images')
    list_display_links = ('title', 'manufacturer')
    search_fields = ('title', 'manufacturer')


admin.site.register(Bd, BdAdmin)