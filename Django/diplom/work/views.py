from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse  # использов. тега шаблона url
from django.views.generic import TemplateView  # Рендер шаблона/классы-представления
from django.contrib.auth.models import User  # доступ к пользователям
from django.core.exceptions import ObjectDoesNotExist #

from .models import Bd

import random

def smartphones(request):
    template = 'work/smartphones.html'
    phones = Bd.objects.all()
    context = {'phones': phones}
    return render(request, template, context)

def phone(request, bd_id):
    template = 'work/phone.html'
    phone = Bd.objects.get(pk=bd_id)
    context = {'phone': phone}
    return render(request, template, context)

def accessories(request):
    template = 'work/empty_section.html'
    context= {}
    return render(request, template, context)

def index(request):
    template = 'work/index.html'
    phones = Bd.objects.all()
    # реализована выборка случайных 3 телефонов
    choices = random.sample(list(phones), 3)
    context = {'phones': choices}
    return render(request, template, context)

class RegisterView(TemplateView):
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                try:
                    _ = User.objects.get(username='1112')
                except ObjectDoesNotExist:
                    return render(request, self.template_name)
                else:
                    User.objects.create_user(username, email, password)  # создание пользователя
                    return redirect(reverse("auth_login"))  # возврат на авторизацию

