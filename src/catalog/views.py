from django.shortcuts import render
from django.views import generic
from . import models

#ATHOR VIEWS
class AthorList(generic.ListView):
    model = models.Athor

class AthorCreate(generic.CreateView):
    model = models.Athor
    fields = ["name", "biography"]
    template_name = "catalog/athor_create.html"

class AthorUpdate(generic.UpdateView):
    model = models.Athor
    fields = ["name", "biography"]
    template_name = "catalog/athor_update.html"

class AthorDetail(generic.DetailView):
    model = models.Athor

class AthorDelete(generic.DeleteView):
    model = models.Athor
    success_url = "/athor_list/"

#SERIES VIEWS
class SeriaList(generic.ListView):
    model = models.Series

class SeriaCreate(generic.CreateView):
    model = models.Series
    fields = ["title", "description"]
    template_name = "catalog/series_create.html"

class SeriaUpdate(generic.UpdateView):
    model = models.Series
    fields = ["title", "description"]
    template_name = "catalog/series_update.html"

class SeriaDetail(generic.DetailView):
    model = models.Series

class SeriaDelete(generic.DeleteView):
    model = models.Series
    success_url = "/seria_list/"

#GENRE VIEWS
class GenreList(generic.ListView):
    model = models.Genres

class GenreCreate(generic.CreateView):
    model = models.Genres
    fields = ["title", "description"]
    template_name = "catalog/genres_create.html"

class GenreUpdate(generic.UpdateView):
    model = models.Genres
    fields = ["title", "description"]
    template_name = "catalog/genres_update.html"

class GenreDetail(generic.DetailView):
    model = models.Genres

class GenreDelete(generic.DeleteView):
    model = models.Genres
    success_url = "/genre_list/"

#PUBLISHING VIEWS
class PublishingList(generic.ListView):
    model = models.Publishing

class PublishingCreate(generic.CreateView):
    model = models.Publishing
    fields = ["title", "description"]
    template_name = "catalog/publishing_create.html"

class PublishingUpdate(generic.UpdateView):
    model = models.Publishing
    fields = ["title", "description"]
    template_name = "catalog/publishing_update.html"

class PublishingDetail(generic.DetailView):
    model = models.Publishing

class PublishingDelete(generic.DeleteView):
    model = models.Publishing
    success_url = "/publishing_list/"