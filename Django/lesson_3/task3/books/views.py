from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

import datetime

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)
