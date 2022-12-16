from django import forms
from education.models import Packet
from django.forms import TextInput, DecimalField, IntegerField


class PackageForm(forms.ModelForm):
    class Meta:
        model = Packet
        fields = ('name', 'qty', 'sum')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название пакета'}),
            'qty': TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Кооличество предметов'}),
            'sum': TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Сумма' }),
        }