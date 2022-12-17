from django.db import models
from education.models import Subject, Discount, Packet
from django.db.models import TextChoices


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


class Application(models.Model):
    applicant_name = models.CharField(verbose_name='Имя заявителя', max_length=30)
    applicant_surname = models.CharField(verbose_name='Фамилия заявителя', max_length=30)
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=13)
    school = models.IntegerField(verbose_name='Номер школы', null=True, blank=True,
                                 help_text="Вводить только цифры")
    class_number = models.CharField(verbose_name='Номер класса', max_length=3, null=True, blank=True)
    shift = models.IntegerField(verbose_name='Номер смены', null=True, blank=True,
                                help_text="Вводить только цифры")
    birth_date = models.DateField(verbose_name='Дата рождения', max_length=10, null=True, blank=True,
                                  help_text="Заполнить в формате дд.мм.гггг")
    sex = models.CharField(verbose_name='Пол студента', choices=StudentSex.choices, max_length=100, default='Undefined')
    
    parents_surname = models.CharField(verbose_name='Фамилия родителя', null=True, blank=True, max_length=30)
    parents_name = models.CharField(verbose_name='Имя родителя', max_length=30, null=True, blank=True)
    parents_inn = models.IntegerField(verbose_name='ИНН родителя', max_length=12, null=True, blank=True,
                                help_text="Вводить только цифры")
    parents_phone = models.CharField(verbose_name='Номер телефона родителя', max_length=13, null=True, blank=True)
    parents_email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    address = models.CharField(verbose_name='Номер телефона родителя', max_length=13, null=True, blank=True,
                               help_text="Вводить через запятую: населенный пункт, улица, номер дома, номер квартиры")
    lesson_time = models.CharField(verbose_name="Желательное время обучения", null=True, blank=True, max_length=250)
    subjects = models.ManyToManyField(to=Subject, related_name='applications', blank=True)
    discount_type = models.ManyToManyField(to=Discount, related_name='applications', blank=True)
    package = models.ManyToManyField(to=Packet, related_name='applications', blank=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    statuses = models.ManyToManyField(
        to=Status,
        through='education.ApplicationStatus',
        related_name='applications')
    is_deleted = models.BooleanField(default=False)
    discounts = models.ManyToManyField(to='education.Discount', related_name='applications')

    def __str__(self):
        return f'Заявка от: {self.applicant_name}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class ApplicationStatus(models.Model):
    application = models.ForeignKey(to=Application, on_delete=models.CASCADE)
    status = models.ForeignKey(to=Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(verbose_name='Примечание', max_length=150, blank=True)

    def __str__(self):
        return f'{self.application} - {self.status}'

    class Meta:
        verbose_name = 'Установленный статус заявки'
        verbose_name_plural = 'Установленные статусы заявок'
