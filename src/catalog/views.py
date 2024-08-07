from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models

#ATHOR VIEWS
class AthorList(generic.ListView):
    model = models.Athor

class AthorCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Athor
    fields = ["name", "biography"]
    template_name = "catalog/athor_create.html"
    permission_required = "catalog.create_athor"

class AthorUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Athor
    fields = ["name", "biography"]
    template_name = "catalog/athor_update.html"
    permission_required = "catalog.change_athor"

class AthorDetail(generic.DetailView):
    model = models.Athor

class AthorDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Athor
    success_url = reverse_lazy("catalog:athor_list")
    permission_required = "catalog.delete_athor"

#SERIES VIEWS
class SeriaList(generic.ListView):
    model = models.Series

class SeriaCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Series
    fields = ["title", "description"]
    template_name = "catalog/series_create.html"
    permission_required = "catalog.create_seria"

class SeriaUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Series
    fields = ["title", "description"]
    template_name = "catalog/series_update.html"
    permission_required = "catalog.change_seria"

class SeriaDetail(generic.DetailView):
    model = models.Series


class SeriaDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Series
    success_url = reverse_lazy("catalog:seria_list")
    permission_required = "catalog.delete_seria"

#GENRE VIEWS
class GenreList(generic.ListView):
    model = models.Genres

class GenreCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Genres
    fields = ["title", "description"]
    template_name = "catalog/genres_create.html"
    permission_required = "catalog.create_genre"

class GenreUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Genres
    fields = ["title", "description"]
    template_name = "catalog/genres_update.html"
    permission_required = "catalog.change_genre"

class GenreDetail(generic.DetailView):
    model = models.Genres

class GenreDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Genres
    success_url = reverse_lazy("catalog:genre_list")
    permission_required = "catalog.delete_genre"

#PUBLISHING VIEWS
class PublishingList(generic.ListView):
    model = models.Publishing

class PublishingCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Publishing
    fields = ["title", "description"]
    template_name = "catalog/publishing_create.html"
    permission_required = "catalog.create_publishing"

class PublishingUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Publishing
    fields = ["title", "description"]
    template_name = "catalog/publishing_update.html"
    permission_required = "catalog.change_publishing"

class PublishingDetail(generic.DetailView):
    model = models.Publishing

class PublishingDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Publishing
    success_url = reverse_lazy("catalog:publishing_list")
    permission_required = "catalog.delete_publishing"
