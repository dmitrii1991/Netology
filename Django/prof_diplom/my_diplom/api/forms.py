from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=150, label='Email', label_suffix='')
    password = forms.CharField(max_length=100, label='Пароль', label_suffix='')


class ForgotForm(forms.Form):
    email = forms.EmailField(max_length=150, label='Email', label_suffix='')
