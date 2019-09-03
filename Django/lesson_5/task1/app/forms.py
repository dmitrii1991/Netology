from django import forms

class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    rate = forms.CharField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean_rate(self):
        rate = int(self.cleaned_data.get('rate'))
        if rate > 100 or rate < 0:
            raise forms.ValidationError("неверная ставка")
        return rate

    def clean_months_count(self):
        months_count = int(self.cleaned_data.get('months_count'))
        if months_count > 60 or months_count < 0 :
            raise forms.ValidationError("неверный срок")
        return months_count