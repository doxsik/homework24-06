from rest_framework import viewsets
from . import models
from . import serializers

class BookInCartViewSet(viewsets.ModelViewSet):
    queryset = models.BookInCart.objects.all()
    serializer_class = serializers.BookInCartSerializer