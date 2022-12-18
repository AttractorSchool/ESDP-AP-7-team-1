from django import forms
from education.models import Application, Subject, Status, Discount, StudentSex

# all_statuses = Status.objects.values()
# STATUS_CHOICES = [(d['id'], d['name']) for d in all_statuses]


class ApplicationEditForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Желаемые предметы',
                                              required=True, queryset=Subject.objects.all())
    sex = forms.ChoiceField(label='Пол',choices=StudentSex.choices)
    # statuses = forms.ChoiceField(label='Статус', choices=STATUS_CHOICES)

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
                  'discounts',
                  ]
        widgets = {
            'discounts': forms.SelectMultiple(),
            'statuses': forms.SelectMultiple(),
        }

