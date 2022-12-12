from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from accounts.models import Account
from phonenumber_field.formfields import PhoneNumberField


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)
    email = forms.CharField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='Имя')
    last_name = forms.CharField(required=True, label='Фамилия')
    phone_number = PhoneNumberField(region='KZ')

    class Meta:
        model = get_user_model()
        fields = ('email', 'phone_number', 'password', 'password_confirm', 'first_name', 'last_name')

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


