from django.db import models


class item(models.Model):
    date = models.DateField(verbose_name = 'дата')
    name = models.CharField(max_length=150, verbose_name='название')
    amount = models.PositiveIntegerField(verbose_name='количество')
    distance = models.PositiveIntegerField(verbose_name='расстояние')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['-id']