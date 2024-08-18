from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from . import models

# Create your views here.
# class CustomerProfileDetail(LoginRequiredMixin, generic.DetailView):
#     model = models.CustomerProfile

#     def get_object(self):
#         user = self.request.user
#         profile = models.CustomerProfile.objects.filter(user__pk=user.pk)
#         if not profile:
#             profile = models.CustomerProfile.objects.create(user=user)
#         return profile

class CustomerProfileUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.CustomerProfile
    fields = ["email", "phone", "name", "surname"]

    def get_object(self):
        user = self.request.user
        profile = models.CustomerProfile.objects.filter(user__pk=user.pk).first()
        if not profile:
            profile = models.CustomerProfile.objects.create(user=user)
        return profile