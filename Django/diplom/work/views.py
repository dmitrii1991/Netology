from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse  # использов. тега шаблона url
from django.views.generic import TemplateView  # Рендер шаблона/классы-представления
from django.contrib.auth.models import User  # доступ к пользователям
from django.core.exceptions import ObjectDoesNotExist  # подключение ошибок
from django.contrib.auth import authenticate, login  # доступ к регистрации

from .models import Bd, Review, CartItem, Category, Order

import random
import datetime


def smartphones(request):
    template = 'work/smartphones.html'
    сategory = Category.objects.get(name='Смартфон')
    phones = Bd.objects.filter(сategory=сategory)
    context = {'phones': phones}
    if request.method == 'POST':
        if request.user.is_authenticated:  # связь с данными о пользователе
            pk_bd = request.POST['add_item']
            bd = Bd.objects.get(pk=pk_bd)
            user = User.objects.get(username=request.user.username)  # поиск пользователя
            cart = CartItem.objects.filter(item=pk_bd).filter(user=user).filter(bought=False)  # Поиск необходимой корзины
            if cart:
                cart[0].total_number = cart[0].total_number + 1  # изменение записи
                cart[0].save()  # сохранение
                return redirect(reverse("cart"))
            else:
                # если корзина с этим товаром не обнаруженаЮ то добавляется товар - 1 шт
                new = CartItem.objects.create(user=user, total_number=1, item=bd)
                return redirect(reverse("cart"))
        return redirect(reverse("auth_login"))  # возврат на авторизацию если пользователь не авторизован
    return render(request, template, context)


def phone(request, bd_id):
    template = 'work/phone.html'
    phone = Bd.objects.get(pk=bd_id)
    reviews = Review.objects.filter(bd=bd_id)
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        user_review = Review.objects.filter(author=user).filter(bd=bd_id)
    context = {'phone': phone, 'reviews': reviews, 'user_review': user_review}
    if request.method == 'POST':
        if 'Cart' in request.POST:  # Отправка в корзину
            if request.user.is_authenticated:  # связь с данными о пользователе
                bd = Bd.objects.get(pk=bd_id)
                user = User.objects.get(username=request.user.username)  # поиск пользователя
                cart = CartItem.objects.filter(item=bd_id).filter(user=user).filter(bought=False)  # Поиск необходимой корзины
                if cart:
                    cart[0].total_number = cart[0].total_number + 1  # изменение записи
                    cart[0].save()  # сохранение
                    return redirect(reverse("cart"))
                else:
                    # если корзина с этим товаром не обнаружена, то добавляется товар - 1 шт
                    new = CartItem.objects.create(user=user, total_number=1, item=bd)
                    return redirect(reverse("cart"))
            return redirect(reverse("auth_login"))  # возврат на авторизацию если пользователь не авторизован
        elif 'Rewiev' in request.POST:  # Отправка отзыва
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user.username)
                description = request.POST.get('description')
                mark = request.POST.get('mark')
                if not Review.objects.filter(author=user).filter(text=description):  # грубая проверка на одни теже данные
                    new_review = Review.objects.create(author=user, text=description, score=mark, bd=phone)
            else:
                return redirect(reverse("auth_login"))
    return render(request, template, context)


def accessories(request):
    template = 'work/empty_section.html'
    context = {}
    return render(request, template, context)


def show_cart(request):
    template = 'work/cart.html'
    context = {}
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        all_cart = CartItem.objects.filter(user=user).filter(bought=False)
        if request.method == 'POST':
            if 'order' in request.POST:
                invoice = random.randint(1, 999999999)  # тут можно реализовать методику созд. уникального номера для накладной
                date = datetime.datetime.now()
                order = Order.objects.create(user=user, invoice=invoice, date=date)
                order.cart.add(*all_cart)
                total_number = 0
                for cart in all_cart:
                    total_number = total_number + cart.total_number * cart.item.price
                    cart.bought = True  # Помечаем, что товар заказан, и убираем его из корзины (в буд. можно показвать как историю)
                    cart.save()
                    print(total_number)
                order.total_number = total_number
                order.save()
                all_cart = set()

            elif 'clear' in request.POST:
                pk_cart = request.POST['item']
                CartItem.objects.get(pk=pk_cart).delete()
            elif 'add' in request.POST:
                pk_cart = request.POST['item']
                cart_item = CartItem.objects.get(pk=pk_cart)
                cart_item.total_number = cart_item.total_number + 1
                cart_item.save()
            else:
                pk_cart = request.POST['item']
                cart_item = CartItem.objects.get(pk=pk_cart)
                if cart_item.total_number == 1:
                    cart_item.delete()
                else:
                    cart_item.total_number = cart_item.total_number - 1
                    cart_item.save()

        quantity = len(all_cart)  # количество видов товара в корзине
        if quantity:
            context = {'carts': all_cart, 'quantity': quantity}
        return render(request, template, context)
    return redirect(reverse("auth_login"))  # возврат на авторизацию если пользователь не авторизован


class AddInCart(TemplateView):
    template_cart = "work/cart.html"
    template = 'work/index.html'

    def dispatch(self, request, *args, **kwargs):
        # реализована выборка случайных 3 телефонов
        сategory = Category.objects.get(name='Смартфон')
        phones = Bd.objects.filter(сategory=сategory)
        choices = random.sample(list(phones), 3)

        # реализована выборка случайного товара из категории одеждлы
        сategory = Category.objects.get(name='Одежда')
        clothes = Bd.objects.filter(сategory=сategory)
        choices_cloth = random.choice(list(clothes))

        context = {'phones': choices, "clothes": choices_cloth}
        if request.method == 'POST':
            if request.user.is_authenticated:  # связь с данными о пользователе
                pk_bd = request.POST['add_item']
                bd = Bd.objects.get(pk=pk_bd)
                user = User.objects.get(username=request.user.username)  # поиск пользователя
                cart = CartItem.objects.filter(item=pk_bd).filter(user=user).filter(bought=False)  # Поиск необходимой корзины
                if cart:
                    cart[0].total_number = cart[0].total_number + 1  # изменение записи
                    cart[0].save()                                # сохранение
                    return redirect(reverse("cart"))
                else:
                    # если корзина с этим товаром не обнаруженаЮ то добавляется товар - 1 шт
                    new = CartItem.objects.create(user=user, total_number=1, item=bd)
                    return redirect(reverse("cart"))
            return redirect(reverse("auth_login"))  # возврат на авторизацию если пользователь не авторизован
        return render(request, self.template, context)


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
