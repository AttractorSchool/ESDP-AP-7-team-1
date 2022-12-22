from django import forms
from django.core.exceptions import ValidationError

from accounts.models import Account
from education.models import Grouping
from django.forms import TextInput


class GroupingForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(label='Преподаватель', widget=forms.CheckboxSelectMultiple,
                                              queryset=Account.objects.filter(groups__name='teacher'))
    students = forms.ModelMultipleChoiceField(label='Студенты', required=False, widget=forms.CheckboxSelectMultiple,
                                              queryset=Account.objects.filter(groups__name='student'))

    class Meta:
        model = Grouping
        fields = ('name', 'subject', 'teachers', 'students')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название группы'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('teachers') is not None:
            if len(cleaned_data.get('teachers')) > 1:
                raise ValidationError('Выберете одного преподавателя')
        if cleaned_data.get('students') is not None:
            # for i in cleaned_data.get('students'):
            #     print(i.pk)
            if len(cleaned_data.get('students')) > 12:
                raise ValidationError('В группе может быть не более 12 студентов')
        return cleaned_data
