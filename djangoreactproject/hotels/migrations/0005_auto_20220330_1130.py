# Generated by Django 3.2.12 on 2022-03-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_auto_20220329_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoteloffers',
            name='date_begin',
            field=models.DateField(verbose_name='дата_заезда'),
        ),
        migrations.AlterField(
            model_name='hoteloffers',
            name='date_end',
            field=models.DateField(verbose_name='дата_выезда'),
        ),
    ]