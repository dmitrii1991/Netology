from django.urls import path
from .views import smartphones, phone, accessories, index
from django.contrib.auth.views import LoginView  # авторизация вход
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

urlpatterns = [
    path('', index, name='index'),
    path('smartphones/', smartphones, name='smartphones'),
    path('smartphones/<int:bd_id>/', phone, name='phone'),
    path('smartphones/accessories/', accessories, name='accessories'),
    path('login/', LoginView.as_view(redirect_field_name='redirect_to'), name='auth_login'), # авторизация вход
    # path('signup/', auth.views.signup, name='signup'),
    #
    # path('logout/', auth.views.logout_view, name='logout_view'),
]
