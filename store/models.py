from django.db import models

class Glasses(models.Model):
    title = models.CharField(max_length=50, verbose_name='Модель')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='archives/%Y/%m/%d/')


    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'