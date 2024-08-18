from django.db import models
from django.urls import reverse_lazy
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True)
    cover = models.ImageField(upload_to="books_images/%Y/%m/%d/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    athor = models.ManyToManyField("catalog.Athor", verbose_name=("arthor"))
    seria = models.ManyToManyField("catalog.Series", verbose_name=("seria"))
    genre = models.ManyToManyField("catalog.Genres", verbose_name=("genre"))
    data = models.IntegerField(null=True)
    pages = models.IntegerField(null=True)
    binding = models.TextField(max_length=50, null=True)
    format = models.TextField(max_length=50, null=True)
    isbn = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    for_age = models.IntegerField(null=True)
    publishing = models.ManyToManyField("catalog.Publishing", verbose_name=("publishing"))
    in_stock = models.IntegerField(null=True)
    active = models.BooleanField(default=False)
    rating = models.IntegerField(null=True)
    data_created = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    data_changed = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    
    def get_absolute_url(self):
        return reverse_lazy("books:book_detail", kwargs = {"pk":self.pk})
    
    def __str__(self):
        return self.title