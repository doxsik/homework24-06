from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from . import models

# Create your views here.

class BookList(generic.ListView):
    model = models.Book

class BookCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Book
    fields = '__all__'
    template_name = "books/book_create.html"
    permission_required = "books.create_book"
    

class BookUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Book
    fields = '__all__'
    template_name = "books/book_update.html"
    permission_required = "books.change_book"

class BookDetail(generic.DetailView):
    model = models.Book

class BookDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Book
    success_url = reverse_lazy("books:book_list")
    permission_required = "books.delete_book"
