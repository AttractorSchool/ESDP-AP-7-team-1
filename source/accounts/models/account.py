from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import AccountManager


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар',
    )
    username = None
    phone_number = PhoneNumberField(
        unique=True,
        null=False,
        blank=False,
    )
    teach_subjects = models.ManyToManyField(to='education.Subject', related_name='teachers', blank=True)
    application = models.ForeignKey(
        verbose_name="Заявка",
        to='applications.Application',
        related_name='accounts',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.get_full_name()}'
