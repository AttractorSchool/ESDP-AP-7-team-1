from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import TextChoices

from phonenumber_field.modelfields import PhoneNumberField


class Status(models.Model):
    """Возможные статусы заявок"""
    name = models.CharField(verbose_name='Название', max_length=30, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доступный статус заявки'
        verbose_name_plural = 'Доступные статусы заявок'


class StudentSex(TextChoices):
    MALE = 'MALE', 'Er bala'
    FEMALE = 'FEMALE', 'Qyz bala'


def validate_length(value):
    an_integer = value
    a_string = str(an_integer)
    if len(a_string) > 12:
        raise ValidationError(_('инн более 12 символов'))
    elif len(a_string) < 12:
        raise ValidationError(_('инн менее 12 символов'))


class Application(models.Model):
    """Созданные заявки пользователями"""
    applicant_name = models.CharField(verbose_name='Имя ученика', max_length=30)
    applicant_surname = models.CharField(verbose_name='Фамилия ученика', max_length=30)
    email = models.EmailField(verbose_name='Электронная почта ученика', blank=True)
    phone = PhoneNumberField(
        unique=False,
        null=False,
        blank=False,
    )
    school = models.IntegerField(verbose_name='Номер школы', null=True, blank=True, validators=[MinValueValidator(0)],
                                 help_text="Вводить только цифры")
    class_number = models.CharField(verbose_name='Номер класса', max_length=3, null=True, blank=True)
    shift = models.IntegerField(verbose_name='Номер смены', null=True, blank=True,
                                help_text="Вводить только цифры")
    birth_date = models.DateField(verbose_name='Дата рождения ученика', max_length=10, null=True, blank=True,
                                  help_text="Заполнить в формате дд.мм.гггг")
    sex = models.CharField(verbose_name='Пол ученика', choices=StudentSex.choices, max_length=100, default='Undefined')
    parents_surname = models.CharField(verbose_name='Фамилия родителя', null=True, blank=True, max_length=30)
    parents_name = models.CharField(verbose_name='Имя родителя', max_length=30, null=True, blank=True)
    parents_inn = models.PositiveBigIntegerField(verbose_name='ИНН родителя', null=True, blank=True,
                                                 help_text="Вводить только цифры",
                                                 validators=[validate_length, MinValueValidator(0)])
    parents_phone = models.CharField(verbose_name='Номер телефона родителя', max_length=18, null=True, blank=True)
    parents_email = models.EmailField(verbose_name='Электронная почта родителя', null=True, blank=True)
    address = models.CharField(verbose_name='Адрес проживания', max_length=200, null=True, blank=True,
                               help_text="Вводить через запятую: населенный пункт, улица, номер дома, номер квартиры")
    lesson_time = models.CharField(verbose_name="Желательное время обучения", null=True, blank=True, max_length=250)
    subjects = models.ManyToManyField(to='education.Subject', related_name='applications', blank=True)
    sum = models.IntegerField(verbose_name='Cумма пакета', null=True, blank=True, validators=[MinValueValidator(0)])
    contract = models.FileField(verbose_name="Подписанный договор", null=True, blank=True,
                                help_text="Загружать pdf подписанного договора", upload_to='contracts/')
    payed = models.BooleanField(verbose_name="Оплачено", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    statuses = models.ManyToManyField(
        to=Status,
        verbose_name='Статус заявки',
        through='education.ApplicationStatus',
        related_name='applications',
    )
    is_deleted = models.BooleanField(default=False)
    discount = models.ForeignKey(
        verbose_name="Льгота",
        to='education.Discount',
        related_name='applications',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    student = models.OneToOneField(to='accounts.Account', on_delete=models.RESTRICT,
                                   related_name='application_student', blank=True, null=True)
    parent = models.OneToOneField(to='accounts.Account', on_delete=models.SET_NULL,
                                  related_name='application_parent', blank=True, null=True)

    def __str__(self):
        return f'Заявка от: {self.applicant_name}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


class ApplicationStatus(models.Model):
    """Установленные статусы заявок"""
    application = models.ForeignKey(to=Application, on_delete=models.CASCADE, related_name='application_statuses')
    status = models.ForeignKey(to=Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(verbose_name='Примечание', max_length=150, blank=True)
    author = models.ForeignKey(to='accounts.Account', on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f'{self.application} - {self.status}'

    class Meta:
        verbose_name = 'Установленный статус заявки'
        verbose_name_plural = 'Установленные статусы заявок'
        ordering = ['-created_at']

        get_latest_by = 'created_at'
