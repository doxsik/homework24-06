from rest_framework import serializers

from . import models

class BookInCartSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.HyperlinkedRelatedField(view_name='books:book-detail', read_only=True)
    class Meta:
        model = models.BookInCart
        fields = ['id', 'book', 'quantity', 'price']
