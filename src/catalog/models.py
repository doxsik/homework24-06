from django.db import models
from django.urls import reverse

class Athor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return f"/athor_detail/{self.pk}"
    
    
class Series(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return f"/seria_detail/{self.pk}"

class Genres(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return f"/genre_detail/{self.pk}"


class Publishing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return f"/publishing_detail/{self.pk}"