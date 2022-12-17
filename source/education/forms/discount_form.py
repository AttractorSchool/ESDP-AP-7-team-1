from django import forms
from education.models import Discount
from django.forms import TextInput


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ('name', 'discount_amount')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название льготы'}),
            'discount_amount': TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Размер в %'}),
        }