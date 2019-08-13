import csv
from .settings import BUS_STATION_CSV
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page = request.GET.get("page", 1)
    print(page)
    with open(BUS_STATION_CSV, encoding='cp1251') as file:
        reader = csv.DictReader(file)
        total_data = []
        for raw in reader:
            data = {
                'Name': raw['Name'],
                'Street': raw['Street'],
                'District': raw['District']
            }
            total_data.append(data)
        p = Paginator(total_data, 20)

        if int(page) == 1:
            pageDown = 1
            pageUp = int(page) + 1
        elif int(page) == p.num_pages:
            pageDown = int(page) - 1
            pageUp = p.num_pages
        elif int(page) in p.page_range:
            pageUp = int(page) + 1
            pageDown = int(page) - 1
        else:
            return HttpResponse(f'Нет такой страницы. Всего страниц: {p.num_pages}')
        context = {
            'prev_page_url': f'?page={pageDown}',
            'next_page_url': f'?page={pageUp}',
            'current_page': int(page),
            'bus_stations': p.page(int(page)).object_list,
        }

    return render_to_response('index.html', context=context)

