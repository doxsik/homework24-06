from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from . import models

# Create your views here.

class BookList(generic.ListView):
    model = models.Book
    paginate_by = 1

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

class BookSearch(generic.ListView):
    model = models.Book
    paginate_by = 1
    template_name = "books/book_search.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search")
        context["search"] = search
        return context

    def get_queryset(self):
        search = self.request.GET.get("search")
        return models.Book.objects.filter(
            Q(title__icontains=search)|
            Q(for_age__icontains=search)|
            Q(athor__name__icontains=search)|
            Q(genre__title__icontains=search)|
            Q(seria__title__icontains=search)
            )
    