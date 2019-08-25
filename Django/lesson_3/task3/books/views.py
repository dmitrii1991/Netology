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

    books1 = list()
    pages = set()
    for book in books:
        pages.add(str(book.pub_date))
        if str(book.pub_date) == date:
            books1.append(book)

    # p = Paginator(pages, 10)
    pages = list(pages)
    page = pages.index(date)

    if page == 0:
        pageDown = 0
        pageUp = page + 1
    elif page == len(pages) - 1:
        pageDown = page - 1
        pageUp = len(pages) - 1
    elif page in range(1, len(pages)-1):
        pageUp = page + 1
        pageDown = page - 1
    else:
        return HttpResponse('Нет такой даты')
    context = {
        'prev_page_url': f'{pages[pageDown]}/',
        'next_page_url': f'{pages[pageUp]}/',
        'current_page': date,
        'books': books1,
    }



    # context = {'books': books1}
    return render(request, template, context)






