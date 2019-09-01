from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime

def books_view(request, date=None):
    template = 'books/books_list.html'
    books = Book.objects.order_by('-pub_date')

    if not date:
        context = {'books': books}
        return render(request, template, context)

    books_our = books.filter(pub_date=date)
    prev_date = books_our.first()
    next_date = books_our.last()

    if not books_our:
        return HttpResponse('Нет такой даты')

    # return HttpResponse(prev_date)
    context = {
        'prev_page_url': f'{prev_date.pub_date}/',
        'next_page_url': f'{next_date.pub_date}/',
        'current_page': date,
        'books': books_our,
    }


    return render(request, template, context)







