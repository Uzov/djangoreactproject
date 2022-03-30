from django.db import models
from django.contrib.postgres.fields import JSONField


class HotelOffers(models.Model):
    offer_id = models.CharField(verbose_name='ID_предложения', max_length=25, blank=False)
    hotel_id = models.IntegerField(verbose_name='ID_отеля', blank=False)
    price = models.IntegerField(verbose_name='стоимость', blank=False)
    currency = models.CharField(verbose_name='валюта', max_length=3, blank=False)
    acc_name = models.CharField(verbose_name='тип_проживания', max_length=255, blank=False)
    room_name = models.CharField(verbose_name='тип_комнаты', max_length=255, blank=False)
    meal_name = models.CharField(verbose_name='тип_питания', max_length=255, blank=False)
    meal_code = models.CharField(verbose_name='код_питания', max_length=2, blank=False)
    tariff_name = models.CharField(verbose_name='тип_тарифа', max_length=255, blank=False)
    date_begin = models.DateField(verbose_name='дата_заезда', blank=False)
    date_end = models.DateField(verbose_name='дата_выезда', blank=False)
    nights = models.IntegerField(verbose_name='число_ночей', blank=False)
    quote = models.IntegerField(verbose_name='квота', blank=False)
    comission = models.IntegerField(verbose_name='комиссия', blank=False)
    cancellation = JSONField(verbose_name='штраф_за_отмену_бронирования', null=True)

    def __str__(self):
        return f'{self.offer_id} ({self.date_begin} - {self.date_end})'
