from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse  # использов. тега шаблона url
from django.views.generic import TemplateView  # Рендер шаблона/классы-представления
from django.contrib.auth.models import User  # доступ к пользователям
from django.core.exceptions import ObjectDoesNotExist  # подключение ошибок
from django.contrib.auth import authenticate, login  # доступ к регистрации

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


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            # поиск пользователя по почте
            try:
                user_ = User.objects.get(email=email)
            except ObjectDoesNotExist:
                pass
            # Авторизация
            user = authenticate(request, username=user_.username, password=password)
            if user:
                login(request, user)
                return redirect("/prosto/")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class RegisterView(TemplateView):
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            # Провекрка повторную регистрацию
            if password == password2:
                try:
                    _ = User.objects.get(username=username)
                except ObjectDoesNotExist:
                    User.objects.create_user(username, email, password)  # создание пользователя
                    return redirect(reverse("auth_login"))  # возврат на авторизацию
                else:
                    context['error'] = "Такой поользователь есть"

        return render(request, self.template_name, context)
