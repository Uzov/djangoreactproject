from rest_framework import serializers
from .models import HotelOffers, HotelBooking


class OffersSerializer(serializers.ModelSerializer):
    cancellation_info = serializers.JSONField()

    class Meta(object):
        model = HotelOffers
        fields = ('id', 'offer_id', 'hotel_id', 'price', 'currency', 'acc_name', 'room_name', 'meal_name', 'meal_code',
                  'tariff_name', 'date_begin', 'date_end', 'check_in', 'check_out', 'nights', 'quote', 'commission',
                  'cancellation_info')

