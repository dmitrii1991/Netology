from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort_order = request.GET.get('sort')
    sort_orders = {'name': 'name',
                   'min_price': 'price',
                   'max_price': '-price'}
    phones = Phone.objects.all()
    if sort_order in sort_orders:
        phones = phones.order_by(sort_orders[sort_order])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
