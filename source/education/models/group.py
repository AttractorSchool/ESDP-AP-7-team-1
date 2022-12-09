from django.db import models
from education.models import Subject
from accounts.models import Account

class Group(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=20, unique=True)
    subject = models.ForeignKey(to=Subject, related_name='groups', on_delete=models.CASCADE)

    students = models.ManyToManyField(
        to=Account, 
        through='education.StudentGroup',
        )
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    

class StudentGroup(models.Model):
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    enrolled_at = models.DateField(verbose_name='Дата зачисления', blank=True, null=True)
    expelled_at = models.DateField(verbose_name='Дата отчисления', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Студент в группе', default=True)

    def __str__(self):
        return f'{self.group} - {self.student}'

    class Meta():
        verbose_name = 'Студент в группе'
        verbose_name_plural = 'Студенты в группе'
