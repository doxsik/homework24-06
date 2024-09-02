from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    email = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name="Country", blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name="City", blank=True, null=True)
    index = models.IntegerField(verbose_name="Index", blank=True, null=True)
    street_house = models.CharField(max_length=50, verbose_name="Street, house", blank=True, null=True)
    information_to_know = models.TextField(max_length=50, verbose_name="Information to know", blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse_lazy("accounts:customer_profile")
    