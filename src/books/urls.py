from django.urls import path
from . import views as books

app_name = "books"
urlpatterns = [
    path("book_list/", books.BookList.as_view(), name="book_list"),
    path("book_detail/<int:pk>", books.BookDetail.as_view(), name="book_detail"),
    path("book_create/", books.BookCreate.as_view(), name="book_create"),
    path("book_update/<int:pk>", books.BookUpdate.as_view(), name="book_update"),
    path("book_delete/<int:pk>", books.BookDelete.as_view(), name="book_delete"),
]