from django.urls import path, include
from . import views as adminpanel

from . import apiviews

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'orders_list/api-orders', apiviews.OrdersSet)

app_name = "adminpanel"
urlpatterns = [
    path("orders_list/", adminpanel.OrdersList.as_view(), name="orders_list"),
]

urlpatterns = urlpatterns + router.urls