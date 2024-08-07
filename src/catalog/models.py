from django.db import models
from django.urls import reverse_lazy

class Athor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse_lazy("catalog:athor_detail", kwargs={"pk":self.pk})
    
    
class Series(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse_lazy("catalog:seria_detail", kwargs={"pk":self.pk})

class Genres(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse_lazy("catalog:genre_detail", kwargs={"pk":self.pk})


class Publishing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse_lazy("catalog:publishing_detail", kwargs={"pk":self.pk})