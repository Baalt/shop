# Generated by Django 4.0.2 on 2022-02-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_glasses_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30, verbose_name='Имя клиента')),
                ('review', models.TextField(max_length=400, verbose_name='Отзыв')),
                ('image', models.ImageField(upload_to='client/%Y/%m/%d/', verbose_name='Фото клиента')),
            ],
        ),
    ]