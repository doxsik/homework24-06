from django.shortcuts import render
from django.views import generic
from . import models

class AthorList(generic.ListView):
    model = models.Athor

class AthorDetail(generic.DeleteView):
    model = models.Athor
    template_name = "catalog/athor_detail.html"