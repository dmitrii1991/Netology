from django.urls import path
from .views import smartphones, phone, not_realised, AddInCart, RegisterView, LoginView, show_cart, clothes
from django.contrib.auth.views import LogoutView  # выход


urlpatterns = [
    path('', AddInCart.as_view(), name='index'),
    path('cart/', show_cart, name='cart'),
    path('smartphones/', smartphones, name='smartphones'),
    path('clothes/', clothes, name='clothes'),
    path('smartphones/<int:bd_id>/', phone, name='phone'),
    path('not_realised/<int:nr_id>/', not_realised, name='not_realised'),
    path('login/', LoginView.as_view(), name='auth_login'),  # авторизация вход redirect_to - переход по заданному пути
    path('logout/', LogoutView.as_view(redirect_field_name='redirect_to'), name='logout_view'),  # авторизация выход
    path('signup/',  RegisterView.as_view(), name='signup'),
]
