from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    students = Student.objects.prefetch_related('teacher')
    context = {'students': students, }

    return render(request, template, context)
