from django import forms
from education.models import Grouping
from accounts.models import Account
from django.forms import TextInput


class GroupingForm(forms.ModelForm):
    class Meta:
        model = Grouping
        fields = ('name', 'subject')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название группы'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
        }