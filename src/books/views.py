from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.

class BookList(generic.ListView):
    model = models.Book

class BookCreate(generic.CreateView):
    model = models.Book
    fields = '__all__'
    template_name = "books/book_create.html"

class BookUpdate(generic.UpdateView):
    model = models.Book
    fields = '__all__'
    template_name = "books/book_update.html"

class BookDetail(generic.DetailView):
    model = models.Book

class BookDelete(generic.DeleteView):
    model = models.Book
    success_url = "/book_list/"
