from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm




class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'total_reviews']
    search_fields = ['brand', 'model']
    list_filter = ('brand',)
    ordering = ('-id',)


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ['car', 'title']
    search_fields = ['car__brand', 'car__model']
    ordering = ('-id',)







admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
