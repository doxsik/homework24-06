from rest_framework import viewsets
from orders import models
from . import serializers

class OrdersSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrdersSerializer