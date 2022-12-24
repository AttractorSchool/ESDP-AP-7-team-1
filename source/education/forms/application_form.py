from django import forms
from education.models import Application, Subject


class ApplicationSendForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(label='Желаемые предметы', queryset=Subject.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(
                                                  attrs={
                                                      'class': 'subject-check',
                                                  }))
    email = forms.CharField(required=True, label='Email', widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Email',
        }))
    applicant_name = forms.CharField(required=True, label='Имя', widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Имя',
        }))
    applicant_surname = forms.CharField(required=True, label='Фамилия', widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Фамилия',
        }))
    phone = forms.CharField(required=True, label='Телефон', widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg phone-mask',
            'placeholder': 'Телефон',
        }))

    class Meta:
        model = Application
        fields = ('applicant_name', 'applicant_surname', 'email', 'phone', 'subjects')

    def save(self, commit=True):
        application = super().save(commit=True)
        application.save()
        # application.statuses.add('1')
        return application
