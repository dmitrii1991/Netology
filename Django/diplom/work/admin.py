from django.contrib import admin
from .models import Bd, Review, Category, CartItem, Order


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'manufacturer', 'launch', 'description', 'images', 'category')
    list_display_links = ('title', 'manufacturer', 'category')
    search_fields = ('title', 'manufacturer')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'total_number', 'item', 'bought')
    list_filter = ('user', )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'bd', 'text')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'invoice', 'date', 'total_number', 'display_item')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Bd, BdAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
