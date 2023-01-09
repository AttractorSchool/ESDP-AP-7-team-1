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


class TeacherInformation(models.Model):
    user = models.ForeignKey(to='accounts.Account', verbose_name='Преподаватель', related_name='teachers',
                             on_delete=models.CASCADE, null=False, blank=False)
    birth_date = models.DateField(verbose_name='Дата рождения', max_length=10, null=False, blank=False)
    teacher_inn = models.PositiveBigIntegerField(verbose_name='ИНН преподавателя', null=False, blank=False)
    address = models.CharField(verbose_name='Адрес проживания', max_length=200, null=False, blank=False)
    education = models.CharField(verbose_name='Образование', null=False, blank=False, max_length=500)
    subjects = models.ManyToManyField(to='education.Subject', related_name='teacher_subject', blank=False)
