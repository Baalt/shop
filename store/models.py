from django.db import models


class Glasses(models.Model):
    title = models.CharField(max_length=50, verbose_name='Модель')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='archives/%Y/%m/%d/')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'


class CustomerReviews(models.Model):
    client_name = models.CharField(max_length=30, verbose_name='Имя клиента')
    review = models.TextField(max_length=400, verbose_name='Отзыв')
    image = models.ImageField(verbose_name='Фото клиента', upload_to='client/%Y/%m/%d/')

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'