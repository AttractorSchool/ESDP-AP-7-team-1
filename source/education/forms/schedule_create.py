from django import forms
from education.models import Schedule
from django.forms import TextInput, CheckboxInput


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('grouping', 'week_day', 'class_time', 'auditorium')
