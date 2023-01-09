from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from accounts.models import Account
from phonenumber_field.formfields import PhoneNumberField

from applications.forms.application_edit_form import DateInput
from applications.models import validate_length
from education.models import Subject


class TeacherSignUpForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)
    email = forms.CharField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='Имя')
    last_name = forms.CharField(required=True, label='Фамилия')
    birth_date = forms.DateField(widget=DateInput(format='%Y-%m-%d'), required=True, label='Дата рождения')
    phone_number = PhoneNumberField(region='KZ', label='Телефон')
    education = forms.CharField(required=True, label='Образование')
    teacher_inn = forms.IntegerField(label='ИНН преподавателя', required=True,
                                     help_text="Вводить только цифры",
                                     validators=[validate_length, MinValueValidator(0)])
    address = forms.CharField(label='Адрес проживания', max_length=200, required=True,
                              help_text="Вводить через запятую: населенный пункт, улица, номер дома, номер квартиры")
    subjects = forms.ModelMultipleChoiceField(label='Предмет',
                                              queryset=Subject.objects.filter(is_deleted=False),
                                              widget=forms.CheckboxSelectMultiple(
                                                  attrs={
                                                      'class': 'subject-check',
                                                  }))

    class Meta:
        model = get_user_model()
        fields = (
            'email', 'phone_number', 'password', 'password_confirm', 'first_name', 'last_name', 'birth_date',
            'education', 'teacher_inn', 'address', 'subjects')

    def clean(self):
        cleaned_data = super().clean()
        if Account.objects.filter(email=cleaned_data.get('email')).exists():
            raise ValidationError({'email': ('Пользователь с такой почтой уже существует')})
        if Account.objects.filter(phone_number=cleaned_data.get('phone_number')).exists():
            raise ValidationError({'phone_number': ('Пользователь с таким телефоном уже существует')})
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
