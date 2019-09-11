from django.shortcuts import render
from django.http import HttpResponse

from .forms import CalcForm

def calc_view(request):
    template = "app/calc.html"
    if request.method == "GET":
        form = CalcForm(request.GET)
        if form.is_valid():
            initial_fee = float(form.cleaned_data['initial_fee'])
            rate = int(form.cleaned_data['rate'])
            months_count = int(form.cleaned_data['months_count'])
            common_result = initial_fee + initial_fee * rate / 100
            result = (initial_fee + initial_fee * rate / 100) / months_count
            context = {
                'form': form,
                'result': round(result, 2),
                'common_result': round(common_result, 2),
            }
            return render(request, template, context)
        context = {
            'form': form,
        }
        return render(request, template, context)
    else:
        form = CalcForm(request.POST)
        return render(request, template, context)
    return render(request, template, context)
