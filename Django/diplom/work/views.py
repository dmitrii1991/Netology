from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
import random
from .models import Bd

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