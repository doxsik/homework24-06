from django.urls import path, include

from . import apiviews
from . import views as books

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'api-books', apiviews.BookViewSet)


app_name = "books"
urlpatterns = [
    path("main_list/", books.MainView.as_view(), name="main"),
    path("book_list/", books.BookList.as_view(), name="book_list"),
    path("book_detail/<int:pk>", books.BookDetail.as_view(), name="book_detail"),
    path("book_create/", books.BookCreate.as_view(), name="book_create"),
    path("book_update/<int:pk>", books.BookUpdate.as_view(), name="book_update"),
    path("book_delete/<int:pk>", books.BookDelete.as_view(), name="book_delete"),
    path("book_search/", books.BookSearch.as_view(), name="book_search"),
]

urlpatterns = urlpatterns + router.urls