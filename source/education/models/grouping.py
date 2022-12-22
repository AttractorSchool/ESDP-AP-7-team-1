from django.db import models
from education.models import Subject
from accounts.models import Account


class Grouping(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=20, unique=True)
    subject = models.ForeignKey(to=Subject, verbose_name='Название предмета', related_name='groupings', on_delete=models.CASCADE)
    students = models.ManyToManyField(
        to=Account,
        through='education.StudentGrouping',
        verbose_name='Студенты',
        related_name='groupings'
    )
    teachers = models.ManyToManyField(
        to=Account,
        verbose_name='Преподаватели',
        through='education.TeacherGrouping',
        related_name='teachers'
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа обучения'
        verbose_name_plural = 'Группы обучения'


class StudentGrouping(models.Model):
    grouping = models.ForeignKey(to=Grouping, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    enrolled_at = models.DateField(verbose_name='Дата зачисления', blank=True, null=True, auto_now_add=True)
    expelled_at = models.DateField(verbose_name='Дата отчисления', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Студент в группе', default=True)

    def __str__(self):
        return f'{self.grouping} - {self.student}'

    class Meta:
        verbose_name = 'Студент в группе'
        verbose_name_plural = 'Студенты в группе'


class TeacherGrouping(models.Model):
    grouping = models.ForeignKey(to=Grouping, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    started = models.DateField(verbose_name='Начал преподавать', blank=True, null=True)
    finished = models.DateField(verbose_name='Закончил преподавать', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Студент в группе', default=True)

    def __str__(self):
        return f'Группа: {self.grouping} - Преподаватель: {self.teacher}'

    class Meta:
        verbose_name = 'Преподаватель группы'
        verbose_name_plural = 'Преподаватели группы'
