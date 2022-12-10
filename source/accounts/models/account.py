from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import AccountManager
from phonenumber_field.modelfields import PhoneNumberField


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар'
    )
    phone_number = PhoneNumberField(
        unique=True,
        null=False,
        blank=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def str(self):
        return f'{self.email} {self.username}'
