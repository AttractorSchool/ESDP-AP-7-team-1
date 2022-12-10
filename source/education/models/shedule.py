from django.db import models
from education.models import Class

CATEGORY_CHOICES = [
    ('monday', 'Дүйсенбі'),
    ('tuesday', 'Сейсенбі'),
    ('wednesday', 'Сәрсенбі'),
    ('thursday', 'Бейсенбі'),
    ('friday', 'Жұма'),
    ('saturday', 'Сенбі'),
]


class Schedule(models.Model):
    group = models.ForeignKey(to=Class, related_name='schedules', on_delete=models.CASCADE)
    week_day = models.CharField(
        verbose_name='День недели',
        max_length=15,
        choices=CATEGORY_CHOICES
    )
    time_start = models.TimeField(verbose_name='Время начала занятия')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.group} - {self.week_day}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
