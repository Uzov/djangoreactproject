from .config import multitour_token, multitour_url
from .serializers import *
import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from .models import HotelOffers, HotelBooking


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


class HotelsRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    # Allow only authenticated users to access this url
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = OffersSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user.email)
        return Response(serializer.data, status=status.HTTP_200_OK)
