from rest_framework import serializers
from .models import HotelOffers, HotelBooking


class OffersSerializer(serializers.ModelSerializer):
    cancellation_info = serializers.JSONField(allow_null=True)

    class Meta(object):
        model = HotelOffers
        fields = ('id', 'offer_id', 'hotel_id', 'price', 'currency', 'acc_name', 'room_name', 'meal_name', 'meal_code',
                  'tariff_name', 'date_begin', 'date_end', 'check_in', 'check_out', 'nights', 'quote', 'commission',
                  'cancellation_info')


class BookingSerializer(serializers.ModelSerializer):
    persons = serializers.JSONField(allow_null=True)

    class Meta(object):
        model = HotelBooking
        fields = ('id', 'offer_id', 'user_id', 'email', 'persons', 'booking_id', 'is_cancelled')


