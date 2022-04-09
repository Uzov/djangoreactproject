from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
User = settings.AUTH_USER_MODEL


class HotelOffers(models.Model):
    offer_id = models.CharField(verbose_name='ID_предложения', max_length=25, unique=True, blank=False)
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
    check_in = models.TimeField(verbose_name='время_заезда', blank=True, null=True)
    check_out = models.TimeField(verbose_name='время_выезда', blank=True, null=True)
    nights = models.IntegerField(verbose_name='число_ночей', blank=False)
    quote = models.IntegerField(verbose_name='квота', blank=False)
    commission = models.IntegerField(verbose_name='комиссия', blank=False)
    cancellation_info = JSONField(verbose_name='штраф_за_отмену_бронирования', blank=True, null=True)

    def __str__(self):
        return f'{self.offer_id} ({self.date_begin} - {self.date_end})'


class HotelBooking(models.Model):
    offer_id = models.ForeignKey(HotelOffers, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='email', default='default@email', max_length=40, blank=False)
    persons = JSONField(verbose_name='список_доп_проживающих', blank=True, null=True)
    booking_id = models.CharField(verbose_name="код_бронирования", max_length=10, blank=True)
    is_cancelled = models.BooleanField(verbose_name='отмено_бронирование?', default=False, blank=False)

    def __str__(self):
        return f'{self.offer_id} ({self.user_id} - {self.booking_id})'
