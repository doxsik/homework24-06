from django.urls import path, include
from . import views as adminpanel

app_name = "adminpanel"
urlpatterns = [
    path("orders_list/", adminpanel.OrdersList.as_view(), name="orders_list"),
]
