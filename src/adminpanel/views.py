from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from orders import models

# Create your views here.
class OrdersList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model=models.Order
    template_name="adminpanel/orders_list.html"
    permission_required = "orders.view_order"