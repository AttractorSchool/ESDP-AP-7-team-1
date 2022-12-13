from django import forms
from education.models import Application, Subject


class ApplicationSendForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Желаемые предметы',
                                              required=True, queryset=Subject.objects.all())
    email = forms.CharField(required=True, label='Email')
    applicant_name = forms.CharField(required=True, label='Имя')
    applicant_surname = forms.CharField(required=True, label='Фамилия')
    phone = forms.CharField(required=True, label='Телефон')

    class Meta:
        model = Application
        fields = ('applicant_name', 'applicant_surname', 'email', 'phone', 'subjects')
