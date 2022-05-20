from .config import multitour_token, multitour_url
# from .serializers import *
import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .models import HotelBooking
from .serializers import BookingSerializer
import random


# Create your views here.


class CreateHotelsAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)

    # Сохранение предложения отеля при нажатии кнопки "Бронировать"
    def post(self, request):
        headers = {'content-type': 'application/json'}
        offer_request = {
            "header": {
                "token": multitour_token,
                "method": "Hotel.Offer"
            },
            "request": {
                "id": request.data['m_offer_id']
            }
        }

        try:
            req = requests.post(multitour_url, data=json.dumps(offer_request), headers=headers)
            req.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

        offer = req.json()
        is_success = offer['is_success']

        if is_success:
            response = offer['response']
            # Замена ключа в словаре
            response['m_offer_id'] = response.pop('id')

            booking_data = {
                'offer': response,
                'user': request.user.id,
                'email': request.user.email,
                'persons': {},
                'is_cancelled': True
            }

            serializer = BookingSerializer(data=booking_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            err = {
                "error": offer['error']
            }
            return Response(err, status=status.HTTP_404_NOT_FOUND)


class BookingViewset(viewsets.ModelViewSet):
    # Allow any user (authenticated or not) to access this url
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        if request.method == 'GET':
            queryset = HotelBooking.objects.filter(user=request.user.id)
            serializer = BookingSerializer(queryset, many=True)
            # if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingUpdateAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        if request.method == 'PUT':
            data = request.data.get('booking', {})
            offer_data = data.pop('offer')
            # формируем queryset booking
            booking = HotelBooking.objects.filter(offer__m_offer_id=offer_data)
            if len(booking.values('offer_id')) > 0:
                booking.update(is_cancelled=data['is_cancelled'], persons=data['persons'])
                # Эмуляция бронирования
                if not data["is_cancelled"]:
                    booking.update(booking_id=str(random.randint(100000, 999999)))
                if data['is_cancelled']:
                    booking.update(booking_id='')
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        if request.method == 'DELETE':
            data = request.data.get('booking', {})
            offer_data = data.pop('offer')
            # формируем queryset booking
            booking = HotelBooking.objects.filter(offer__m_offer_id=offer_data)
            if len(booking.values('offer_id')) > 0:
                booking.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)