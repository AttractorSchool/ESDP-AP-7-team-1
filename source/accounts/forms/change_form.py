from django import forms
from django.contrib.auth import get_user_model

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'avatar',
            'email',
            'phone_number'
        ]
        labels = {
            'email': 'Email',
            'avatar': 'Фото',
            'phone_number': 'Телефон'
        }