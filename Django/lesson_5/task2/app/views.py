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
    form = ReviewForm
    exist = None
    request.session.setdefault('reviewed_product', [])
    reviewed_product = request.session['reviewed_product']
    if pk not in reviewed_product:
        if request.method == 'POST':
            form = form(request.POST)
            form.is_valid()
            form_review_text = form.cleaned_data['text']
            form_review = Review(text=form_review_text, product=product)
            form_review.save()
            reviewed_product.append(pk)
            request.session['reviewed_product'] = reviewed_product
            exist = True
    else:
        exist = True
    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exist': exist
    }
    return render(request, template, context)

