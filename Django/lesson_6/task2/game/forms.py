from django import forms


class Form_For_Number(forms.Form):
    number = forms.IntegerField(label="Число", widget=forms.TextInput())