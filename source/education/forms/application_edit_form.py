from django import forms
from education.models import Application, Subject, Status

all_statuses = Status.objects.values()
STATUS_CHOICES = [(d['id'], d['name']) for d in all_statuses]


class ApplicationEditForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Желаемые предметы',
                                              required=True, queryset=Subject.objects.all())
    statuses = forms.ChoiceField(label='Статус', choices=STATUS_CHOICES)

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
                  'statuses'
                  ]
