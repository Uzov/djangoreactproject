from django.conf.urls import url
from .views import CreateHotelsAPIView

urlpatterns = [
    url(r'^create/?$', CreateHotelsAPIView.as_view()),
]