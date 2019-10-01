from django.urls import path
from .views import smartphones, phone, accessories, index, RegisterView, LoginView
from django.contrib.auth.views import LogoutView  # выход


urlpatterns = [
    path('', index, name='index'),
    path('smartphones/', smartphones, name='smartphones'),
    path('smartphones/<int:bd_id>/', phone, name='phone'),
    path('smartphones/accessories/', accessories, name='accessories'),
    path('login/', LoginView.as_view(), name='auth_login'),  # авторизация вход redirect_to - переход по заданному пути
    path('logout/', LogoutView.as_view(redirect_field_name='redirect_to'), name='logout_view'),  # авторизация выход
    path('signup/',  RegisterView.as_view(), name='signup'),
    #
    # path('logout/', auth.views.logout_view, name='logout_view'),
]
