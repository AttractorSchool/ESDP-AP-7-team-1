from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Логин',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control form-control-lg',
                                    'placeholder':'Email/номер телефона'
                                }))
    password = forms.CharField(
        label='Пароль', 
        strip=False, 
        required=True, 
        widget=forms.PasswordInput( attrs={
            'class': 'form-control form-control-lg',
            'placeholder':'Пароль'
        })
        )
