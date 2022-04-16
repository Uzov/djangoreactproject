from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings

User = settings.AUTH_USER_MODEL


class HotelOffers(models.Model):
    m_offer_id = models.CharField(verbose_name='ID предложения', max_length=25, unique=True, blank=False)
    hotel_id = models.IntegerField(verbose_name='ID отеля', blank=False)
    price = models.IntegerField(verbose_name='Стоимость', blank=False)
    currency = models.CharField(verbose_name='Валюта', max_length=3, blank=False)
    acc_name = models.CharField(verbose_name='Тип проживания', max_length=255, blank=False)
    room_name = models.CharField(verbose_name='Тип комнаты', max_length=255, blank=False)
    meal_name = models.CharField(verbose_name='Тип питания', max_length=255, blank=False)
    meal_code = models.CharField(verbose_name='Код питания', max_length=2, blank=False)
    tariff_name = models.CharField(verbose_name='Тип тарифа', max_length=255, blank=False)
    date_begin = models.DateField(verbose_name='Дата заезда', blank=False)
    date_end = models.DateField(verbose_name='Дата выезда', blank=False)
    check_in = models.TimeField(verbose_name='Время заезда', blank=True, null=True)
    check_out = models.TimeField(verbose_name='Время выезда', blank=True, null=True)
    nights = models.IntegerField(verbose_name='Число ночей', blank=False)
    quote = models.IntegerField(verbose_name='Квота отеля', blank=False)
    commission = models.IntegerField(verbose_name='Комиссия', blank=False)
    cancellation_info = JSONField(verbose_name='Штраф за отмену бронирования', blank=True, null=True)

    def __str__(self):
        return f'{self.m_offer_id} ({self.date_begin} - {self.date_end})'


class HotelBooking(models.Model):
    offer = models.OneToOneField(HotelOffers, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='email', default='default@email', max_length=40, blank=False)
    persons = JSONField(verbose_name='Список доп. проживающих', blank=True, null=True)
    booking_id = models.CharField(verbose_name="Код бронирования", max_length=10, blank=True)
    is_cancelled = models.BooleanField(verbose_name='Отменено ли бронирование?', default=True, blank=False)

    def __str__(self):
        return f'{self.user} ({self.offer} - {self.is_cancelled})'
