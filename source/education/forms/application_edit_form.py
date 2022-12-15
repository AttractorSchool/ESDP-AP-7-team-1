from django import forms
from education.models import Application, Subject
from django.forms import TextInput, CheckboxInput


class ApplicationEditForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Желаемые предметы',
                                              required=True, queryset=Subject.objects.all())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields[field_name].widget.attrs.update({
                "placeholder": field.label,
                'class': 'form-control form-control-lg'
            })
        self.fields['subjects'].widget.attrs.update({'class': ''},)
            
    class Meta:
        model = Application
        fields = ['applicant_name',
            'applicant_surname', 
            'email', 
            'phone',
            'subjects', 
            'school', 
            'shift', 
            'birth_date', 
            'parents_surname', 
            'parents_name', 
            'parents_phone', 
            'parents_email', 
            'address', 
            'lesson_time',
             ]
    