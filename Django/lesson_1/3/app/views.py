import csv
from .settings import BUS_STATION_CSV
from django.shortcuts import render_to_response, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
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
        numbers_of_rows = len(total_data)
        context = {
            'prev_page_url': None,
            'next_page_url': None,
        }
        i = 1
        show_context_data = []

        while i <= round(numbers_of_rows / 20):
            if i == 1:
                next_page = i + 1
                context = {
                    'prev_page_url': None,
                    'next_page_url': f'?page={next_page}',
                    'current_page': 1,
                    'bus_stations': total_data[0:20],
                }
                show_context_data.append(context)
            elif i == round(numbers_of_rows / 20):
                previous_page = i - 1
                context = {
                    'prev_page_url': f'?page={previous_page}',
                    'next_page_url': None,
                    'current_page': i,
                    'bus_stations': total_data[previous_page * 20:i * 20],
                }
            else:
                previous_page = i - 1
                next_page = i + 1
                context = {
                    'prev_page_url': f'?page={previous_page}',
                    'next_page_url': f'?page={next_page}',
                    'current_page': i,
                    'bus_stations': total_data[i * 10:i * 10 + 20],
                }
            show_context_data.append(context)
            i += 1
        if 'page' in request.GET:
            return render_to_response('index.html', context=show_context_data[int(request.GET['page'])])
        return render_to_response('index.html', context=show_context_data[1])


