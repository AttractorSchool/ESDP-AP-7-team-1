from django import forms
# from django.utils.datastructures import MultiValueDict

from education.models import Application, StudentSex, Subject


# class M2MSelect(forms.Select):
#     def value_from_datadict(self, data, files, name):
#         if isinstance(data, MultiValueDict):
#             return data.getlist(name)
#         return data.get(name, None)


class ApplicationEditForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(label='Предметы к обучению', queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple(
        attrs={
            'class': 'subject-check',
        }))

    sex = forms.ChoiceField(label='Пол', choices=StudentSex.choices)
    phone = forms.CharField(label='Телефон ученика', widget=forms.TextInput(
        attrs={
            'class': 'phone-mask',
            'placeholder': 'Телефон',
        }))
    parents_phone = forms.CharField(label='Телефон родителя', required=False, widget=forms.TextInput(
        attrs={
            'class': 'phone-mask',
            'placeholder': 'Телефон',
        }))
    payed = forms.BooleanField(label='Оплачено', required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'mx-2',
        }))

    class Meta:
        model = Application
        fields = ['applicant_name',
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
                #   'statuses',
                  'contract',
                  'payed',
                  ]
        # widgets = {
        #     'statuses': M2MSelect(),
        # }
