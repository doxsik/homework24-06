from django.urls import path
from . import views as accounts

app_name = "accounts"
urlpatterns = [
    path("profile/", accounts.CustomerProfileUpdate.as_view(), name="customer_profile"),
]