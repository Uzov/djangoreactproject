from rest_framework import serializers
from .models import HotelOffers, HotelBooking
from drf_writable_nested.serializers import WritableNestedModelSerializer


class OffersSerializer(serializers.ModelSerializer):
    cancellation_info = serializers.JSONField(allow_null=True)

    class Meta(object):
        model = HotelOffers
        fields = (
        'id', 'm_offer_id', 'hotel_id', 'price', 'currency', 'acc_name', 'room_name', 'meal_name', 'meal_code',
        'tariff_name', 'date_begin', 'date_end', 'check_in', 'check_out', 'nights', 'quote', 'commission',
        'cancellation_info'
        )


class BookingSerializer(WritableNestedModelSerializer):
    persons = serializers.JSONField(allow_null=True)
    offer = OffersSerializer(many=False, read_only=False)

    class Meta(object):
        model = HotelBooking
        fields = ('offer', 'user', 'email', 'persons', 'booking_id', 'is_cancelled')
