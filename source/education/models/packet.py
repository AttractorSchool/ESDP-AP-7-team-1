from django.db import models


class Packet(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30, unique=True)
    qty = models.PositiveIntegerField(verbose_name='Количество', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    sum = models.PositiveIntegerField(verbose_name='Сумма', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пакет предметов'
        verbose_name_plural = 'Пакеты предметов'
