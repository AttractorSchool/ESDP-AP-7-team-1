from django import forms

from phonenumber_field.formfields import PhoneNumberField

from education.models import Application, StudentSex, Subject, ApplicationStatus


SHIFTS = ((1, 1), (2, 2), (3, 3))
LESSONS_TIME = (('13:30', '13:30'), ('15:00', '15:00'), ('16:30', '16:30'))


class DateInput(forms.DateInput):
    input_type = 'date'


class ApplicationCustomEditForm(forms.ModelForm):
    """Форма редактирования общих данных заявки"""
    subjects = forms.ModelMultipleChoiceField(label='Предметы к обучению', queryset=Subject.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(
                                                  attrs={
                                                      'class': 'subject-check',
                                                  }))

    sex = forms.ChoiceField(label='Пол', choices=StudentSex.choices)
    phone = PhoneNumberField(region='KZ', label='Телефон', required=True)
    parents_phone = forms.CharField(label='Телефон родителя', required=False, widget=forms.TextInput(
        attrs={
            'class': 'phone-mask',
            'placeholder': 'Телефон',
        }))
    shift = forms.ChoiceField(label='Смена', choices=SHIFTS, required=False, widget=forms.Select)
    lesson_time = forms.ChoiceField(label='Желательное время', choices=LESSONS_TIME, required=False,
                                    widget=forms.Select)
    birth_date = forms.DateField(widget=DateInput(format='%Y-%m-%d'), required=False, label='День рождения')


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
