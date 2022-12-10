from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Логин',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Введите почту, либо номер телефона в формате "+78912345678"'}))
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
