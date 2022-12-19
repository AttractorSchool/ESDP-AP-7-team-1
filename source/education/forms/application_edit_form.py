from django import forms
from django.utils.datastructures import MultiValueDict

from education.models import Application, StudentSex, Subject, Discount

# all_statuses = Status.objects.values()
# STATUS_CHOICES = [(d['id'], d['name']) for d in all_statuses]


class M2MSelect(forms.Select):
    def value_from_datadict(self, data, files, name):
        if isinstance(data, MultiValueDict):
            return data.getlist(name)
        return data.get(name, None)


class ApplicationEditForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Желаемые предметы',
                                              required=True, queryset=Subject.objects.all())
    discount = forms.ModelChoiceField(queryset=Discount.objects.all(), required=False)
    sex = forms.ChoiceField(label='Пол', choices=StudentSex.choices)
    # statuses = forms.ChoiceField(label='Статус', choices=STATUS_CHOICES)
    phone = forms.CharField(required=True, label='Телефон', widget=forms.TextInput(
        attrs={
            'class': 'phone-mask',
            'placeholder': 'Телефон',
        }))
    parents_phone = forms.CharField(required=True, label='Телефон', widget=forms.TextInput(
        attrs={
            'class': 'phone-mask',
            'placeholder': 'Телефон',
        }))

    class Meta:
        model = Application
        fields = ['applicant_name',
                  'applicant_surname',
                  'email',
                  'phone',
                  'subjects',
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
                  'sum',
                  'contract',
                  'statuses',
                  'discount',
                  ]
        widgets = {
            'statuses': M2MSelect(),
        }
