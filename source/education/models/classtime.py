from django.db import models


class ClassTime(models.Model):
    time_start = models.TimeField(verbose_name='Время начала занятия')
    time_end = models.TimeField(verbose_name='Время окончания занятия')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.time_start)

    class Meta:
        verbose_name = 'Время занятия'
        verbose_name_plural = 'Время занятий'
