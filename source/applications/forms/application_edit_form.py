from django import forms
from django.forms.renderers import DjangoTemplates

from phonenumber_field.formfields import PhoneNumberField

from applications.models import Application, ApplicationStatus, StudentSex 

from education.models import Subject


SHIFTS = ((1, 1), (2, 2))
LESSONS_TIME = (('13:30', '13:30'), ('15:00', '15:00'), ('16:30', '16:30'))


class DateInput(forms.DateInput):
    input_type = 'date'


# class CheckboxSelectMultipleWithoutLabels(forms.CheckboxSelectMultiple):

#     def render(self, name: str, value, attrs, renderer: DjangoTemplates):
#         # Call the original render method
#         html = super().render(name, value, attrs, renderer)
#         # Split the HTML into parts
#         parts = html.split('\n')
#         print(parts)
#         # Insert the label before the input
#         parts.insert(-2, '<label')
#         # Join the parts back together
#         return '\n'.join(parts)


class ApplicationCustomEditForm(forms.ModelForm):
    """Форма редактирования общих данных заявки"""
    subjects = forms.ModelMultipleChoiceField(label='Предметы к обучению',
                                              queryset=Subject.objects.filter(is_deleted=False),
                                              widget=forms.CheckboxSelectMultiple(
                                                  attrs={
                                                      'class': 'subject-check',
                                                  }))

    sex = forms.ChoiceField(label='Пол', choices=StudentSex.choices,
                            widget=forms.Select(attrs={'class': 'form-control'}))
    phone = PhoneNumberField(region='KZ', label='Телефон', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    parents_phone = forms.CharField(label='Телефон родителя', required=False, widget=forms.TextInput(
        attrs={
            'class': 'phone-mask form-control',
            'placeholder': 'Телефон',
        }))
    shift = forms.ChoiceField(label='Смена', choices=SHIFTS, required=False,
                              widget=forms.Select(attrs={'class': 'form-control'}))
    lesson_time = forms.ChoiceField(label='Желательное время', choices=LESSONS_TIME, required=False,
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(widget=DateInput(format='%Y-%m-%d', attrs={'class': 'form-control'}), required=False, label='Дата рождения')

    class Meta:
        model = Application
        fields = [
            'applicant_name',
            'applicant_surname',
            'email',
            'phone',
            'school',
            'class_number',
            'shift',
            'birth_date',
            'sex',
            'parents_surname',
            'parents_name',
            'parents_inn',
            'parents_phone',
            'parents_email',
            'address',
            'lesson_time',
            'subjects',
            'discount',
            'sum',
        ]
        widgets = {
            'applicant_name':    forms.TextInput(attrs={'class': 'form-control'}),
            'applicant_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email':             forms.TextInput(attrs={'class': 'form-control'}),
            'school':            forms.TextInput(attrs={'class': 'form-control'}),
            'class_number':      forms.TextInput(attrs={'class': 'form-control'}),
            'parents_surname':   forms.TextInput(attrs={'class': 'form-control'}),
            'parents_name':   forms.TextInput(attrs={'class': 'form-control'}),
            'parents_inn':   forms.TextInput(attrs={'class': 'form-control'}),
            'parents_email':   forms.TextInput(attrs={'class': 'form-control'}),
            'address':   forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'discount':   forms.Select(attrs={'class': 'form-control', 'rows': '3'}),
            'sum':   forms.NumberInput(attrs={'class': 'form-control', 'rows': '3'}),
        }


class ApplicationContractEditForm(forms.ModelForm):
    """Форма редактирования договора заявки"""

    class Meta:
        model = Application
        fields = [
            'contract',
            ]


class ApplicationPayedEditForm(forms.ModelForm):
    """Форма редактирования оплаты заявки"""

    payed = forms.BooleanField(label='Оплачено', required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'mx-2',
        }))

    class Meta:
        model = Application
        fields = [
            'payed',
            ]


class ApplicationRejectForm(forms.ModelForm):
    """Форма отклонения заявки"""

    class Meta:
        model = ApplicationStatus
        fields = [
            'note',
            ]
