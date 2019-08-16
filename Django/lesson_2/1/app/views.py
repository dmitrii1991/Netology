from django.shortcuts import render
from django.http import HttpResponse
from .settings import INFLATION_RUSSIA_CSV
import csv

def inflation_view(request):
    template_name = 'inflation.html'

    with open(INFLATION_RUSSIA_CSV, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        total_data = {}
        keys = list(reader.__iter__().__next__().keys())


        for raw in reader:
            data = {key: float(raw[key]) for key in keys[1:]}
            total_data[raw[keys[0]]] = data

    context = {
        'total_data': total_data,
        'keys': keys,
               }
    # return HttpResponse(f'Нет такой страницы. Всего страниц')
    return render(request, template_name, context)