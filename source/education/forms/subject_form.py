from django import forms
from education.models import Subject
from django.forms import TextInput, CheckboxInput


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'is_required')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название предмета'}),
            'is_required': CheckboxInput(attrs={'class': 'form-check-input'})
        }