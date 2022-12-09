from django.db import models


class Subject(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
