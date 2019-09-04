from django import forms

from .widgets import AjaxInputWidget
from .models import City
from datetime import datetime, timedelta

class SearchTicket(forms.Form):
    city_from = forms.CharField(widget=AjaxInputWidget(url='api/city_ajax'), label='Город отправления')
    city_to = forms.ModelChoiceField(queryset=City.objects.all(), label='Город назначения')
    depart = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.today() + timedelta(days=14))
