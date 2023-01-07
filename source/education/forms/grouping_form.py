from django import forms
from django.core.exceptions import ValidationError

from accounts.models import Account
from education.models import Grouping
from django.forms import TextInput


class GroupingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Grouping.objects.filter(is_deleted=False)

    class Meta:
        model = Grouping
        fields = ('name', 'subject')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название группы'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
        }
