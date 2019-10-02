from django.contrib import admin

from .models import Bd, Review, Category

class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'manufacturer', 'launch', 'description', 'images')
    list_display_links = ('title', 'manufacturer')
    search_fields = ('title', 'manufacturer')


admin.site.register(Bd, BdAdmin)
admin.site.register(Review)
admin.site.register(Category)