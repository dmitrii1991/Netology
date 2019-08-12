from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
import os

def Counter(key=None, status=False):
    '''
    ПОдсчитывает количество переходов или выводит статистику
    :param key: подсчет по запросу
    :param status: вывод статистики
    :return:
    '''
    dirname = os.path.dirname(__file__)
    path, _ = os.path.split(dirname)
    datafile = open(os.path.join(path, 'res/data.json'))
    data = json.load(datafile)

    if status == True:
        datafile.close()
        return data

    if key in ['original', 'test', 'from-landing-test', 'from-landing-original']:
        data[key] += 1
        datafile.close()
        datafile = open(os.path.join(path, 'res/data.json'), 'w')
        json.dump(data, datafile, indent=4)
        datafile.close()

def index(request):
    func = {
        'original': render_to_response('index.html'),
        'test': render_to_response('index.html'),
        'nothing': HttpResponse("Упс, ошибочка!"),
    }
    type_of_page = request.GET.get('from-landing', 'nothing')
    Counter('from-landing-' + type_of_page)
    return func.get(type_of_page, func['nothing'])


def landing(request):
    func = {
        'original': render_to_response('landing.html'),
        'test': render_to_response('landing_alternate.html'),
        'nothing': HttpResponse("Упс, ошибочка!"),
    }
    type_of_page = request.GET.get('ab-test-arg', 'nothing')
    Counter(type_of_page)
    return func.get(type_of_page, func['nothing'])


def stats(request):
    data = Counter(status=True)
    try:
        original = round(data['from-landing-original']/data['original'], 1)
    except ZeroDivisionError:
        original = 'невозможно посчитать'
    try:
        test = round(data['from-landing-test'] / data['test'], 1)
    except ZeroDivisionError:
        test = 'невозможно посчитать'

    return render_to_response('stats.html', context={
        'test_conversion': test,
        'original_conversion': original,
    })
