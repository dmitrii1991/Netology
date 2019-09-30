from django.urls import path
from .views import smartphones, phone, accessories, index

urlpatterns = [
    path('', index, name='index'),
    path('smartphones/', smartphones, name='smartphones'),
    path('smartphones/<int:bd_id>/', phone, name='phone'),
    path('smartphones/accessories/', accessories, name='accessories'),
]
