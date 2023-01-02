from django.db import models

from education.models import Grouping

CATEGORY_CHOICES = [
    ('monday', 'Дүйсенбі'),
    ('tuesday', 'Сейсенбі'),
    ('wednesday', 'Сәрсенбі'),
    ('thursday', 'Бейсенбі'),
    ('friday', 'Жұма'),
    ('saturday', 'Сенбі'),
]


class Schedule(models.Model):
    grouping = models.ForeignKey(to=Grouping, related_name='schedules', on_delete=models.CASCADE,
                                 verbose_name='Группа', blank=True)
    week_day = models.CharField(
        verbose_name='День недели',
        max_length=15,
        choices=CATEGORY_CHOICES,
    )
    class_time = models.ForeignKey(to='education.ClassTime', related_name='schedules',
                                   on_delete=models.CASCADE, null=True, verbose_name='Номер урока')
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    auditorium = models.ForeignKey(to='education.Auditorium', related_name='schedules',
                                   on_delete=models.CASCADE, null=True, verbose_name='Номер аудитории')

    def __str__(self):
        return f'{self.grouping} - {self.week_day} - {self.auditorium}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
