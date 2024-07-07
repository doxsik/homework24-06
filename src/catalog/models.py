from django.db import models

class Athor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
class Series(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class Genres(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class Publishing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"
