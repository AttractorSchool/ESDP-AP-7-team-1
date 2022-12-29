from django.db import models


class Time(models.Model):
    time_start = models.TimeField(verbose_name='Время начала занятия')
    time_end = models.TimeField(verbose_name='Время окончания занятия')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.time_start

    class Meta:
        verbose_name = 'Время занятия'
        verbose_name_plural = 'Время занятия'



