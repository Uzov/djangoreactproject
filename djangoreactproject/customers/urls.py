from django.conf.urls import url
from .views import customers_list, customers_detail

urlpatterns = [
    url(r'^list/?$', customers_list),
    url(r'^detail/(?P<pk>[0-9]+)$', customers_detail),
    ]