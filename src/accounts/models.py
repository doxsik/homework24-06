from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class CustomerProfil(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    password = models.OneToOneField(User, related_name="profile", on_delete=models.PROTECT)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=9)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    group = models.OneToOneField(Group, related_name="group", on_delete=models.SET_NULL)

    
    