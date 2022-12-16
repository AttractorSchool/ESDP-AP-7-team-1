from django.db import models


class Package(models.Model):
    title = models.CharField(verbose_name='Название', max_length=30, unique=True),
    qty = models.PositiveIntegerField(verbose_name='Количество', blank=True, null=True)
    sum = models.DecimalField(verbose_name='Сумма', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пакет'
        verbose_name_plural = 'Пакеты'