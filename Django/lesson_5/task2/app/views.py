from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

# from django.http import HttpResponse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()
    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.all().filter(product=product)
    if 'reviewed_products' not in request.session:
        request.session['reviewed_products'] = list()
    form = ReviewForm
    if request.method == 'POST':
        request.session['reviewed_products'].append(product)
        request.session.save()
        review_ans = request.POST['text'] # чтение
        review = Review(text=review_ans, product=product)  # запись
        review.save()

    context = {
        'form': form,
        'product': product,
        'is_review_exist': True,
    }

    if product in request.session['reviewed_products']:# проверка
        context = {
            'form': form,
            'product': product,
            'reviews': reviews,
        }

    return render(request, template, context)
