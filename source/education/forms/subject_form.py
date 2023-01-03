from django import forms
from django.forms import TextInput

from education.models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название предмета'}),
        }
