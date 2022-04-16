from django.conf.urls import url
from .views import CreateHotelsAPIView, BookingViewset, BookingUpdateAPIView

urlpatterns = [
    url(r'^create/?$', CreateHotelsAPIView.as_view()),
    url(r'^list/?$', BookingViewset.as_view({'get': 'list'})),
    url(r'^update/?$', BookingUpdateAPIView.as_view()),
]
