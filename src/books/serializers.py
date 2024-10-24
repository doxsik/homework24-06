from rest_framework import serializers

from . import models

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'price']