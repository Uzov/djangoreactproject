from rest_framework import serializers
from .models import HotelOffers


class OffersSerializer(serializers.ModelSerializer):
    cancellation_info = serializers.JSONField(allow_null=True)
    persons = serializers.JSONField(allow_null=True)

    class Meta(object):
        model = HotelOffers
        fields = ('id', 'm_offer_id', 'hotel_id', 'price', 'currency', 'acc_name', 'room_name', 'meal_name', 'meal_code',
                  'tariff_name', 'date_begin', 'date_end', 'check_in', 'check_out', 'nights', 'quote', 'commission',
                  'cancellation_info', 'user_id', 'email', 'persons', 'booking_id', 'is_cancelled')
