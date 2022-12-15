from django.db import models
from education.models import Subject


class Status(models.Model):
    """Возможные статусы заявок"""
    name = models.CharField(verbose_name='Название', max_length=30, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доступный статус заявки'
        verbose_name_plural = 'Доступные статусы заявок'


class Application(models.Model):
    applicant_name = models.CharField(verbose_name='Имя заявителя', max_length=30)
    applicant_surname = models.CharField(verbose_name='Фамилия заявителя', max_length=30)
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=13)
    school = models.IntegerField(verbose_name='Номер школы', max_length=5, null=True, blank=True, help_text="Вводить только цифры")
    shift = models.IntegerField(verbose_name='Номер смены', max_length=2, null=True, blank=True, help_text="Вводить только цифры")
    birth_date = models.DateField(verbose_name='Дата рождения', max_length=10, null=True, blank=True, help_text="Заполнить в формате дд.мм.гггг")
    parents_surname = models.CharField(verbose_name='Фамилие родителя', null=True, blank=True, max_length=30)
    parents_name = models.CharField(verbose_name='Имя родителя', max_length=30, null=True, blank=True)
    parents_phone = models.CharField(verbose_name='Номер телефона родителя', max_length=13, null=True, blank=True)
    parents_email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    address = models.CharField(verbose_name='Номер телефона родителя', max_length=13, null=True, blank=True, help_text="Вводить через запятую: населеный пункт, улица, номер дома, номер квартиры")
    lesson_time = models.CharField(verbose_name="Жедательное время обучения", null=True, blank=True, max_length=250)
    subjects = models.ManyToManyField(to=Subject, related_name='applications', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    statuses = models.ManyToManyField(
        to=Status,
        through='education.ApplicationStatus',
        related_name='applications', )
    is_deleted = models.BooleanField(default=False)

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
