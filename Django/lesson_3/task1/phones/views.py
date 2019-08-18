from django.shortcuts import render
from .models import Phone
from django.http import HttpResponse



def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    context = {'phones': phones}

    return render(
        request,
        template,
        context
    )
