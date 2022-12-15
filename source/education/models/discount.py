from django.db import models


class Discount(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    discount_amount = models.PositiveIntegerField(verbose_name='Размер %')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Льгота'
        verbose_name_plural = 'Льготы'
