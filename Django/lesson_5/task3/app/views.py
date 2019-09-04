import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    req = request.GET.get('term')
    key_lower = req.lower()
    results = cache.get(key_lower)

    if results is None:
        results = []
        cities = City.objects.all()
        for city in cities:
            if req in city.name.lower():
                results.append(city.name)
        cache.set(key_lower, results)

    return JsonResponse(results, safe=False)