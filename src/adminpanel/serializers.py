from rest_framework import serializers

from orders import models

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Order
        fields = ['id', 'phone', 'adress', 'data_created', 'delivery_data', 'status']
