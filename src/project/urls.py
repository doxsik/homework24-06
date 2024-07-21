"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from testapp import views as testapp
from catalog import views as catalog
from books import views as books
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", testapp.home_page),
    #ATHOR URLS
    path("athor_list/", catalog.AthorList.as_view()),
    path("athor_detail/<int:pk>", catalog.AthorDetail.as_view()),
    path("athor_create/", catalog.AthorCreate.as_view()),
    path("athor_update/<int:pk>", catalog.AthorUpdate.as_view()),
    path("athor_delete/<int:pk>", catalog.AthorDelete.as_view()),
    #SERIA URLS
    path("seria_list/", catalog.SeriaList.as_view()),
    path("seria_detail/<int:pk>", catalog.SeriaDetail.as_view()),
    path("seria_create/", catalog.SeriaCreate.as_view()),
    path("seria_update/<int:pk>", catalog.SeriaUpdate.as_view()),
    path("seria_delete/<int:pk>", catalog.SeriaDelete.as_view()),
    #GENRE URLS
    path("genre_list/", catalog.GenreList.as_view()),
    path("genre_detail/<int:pk>", catalog.GenreDetail.as_view()),
    path("genre_create/", catalog.GenreCreate.as_view()),
    path("genre_update/<int:pk>", catalog.GenreUpdate.as_view()),
    path("genre_delete/<int:pk>", catalog.GenreDelete.as_view()),
    #PUBLISHING URLS
    path("publishing_list/", catalog.PublishingList.as_view()),
    path("publishing_detail/<int:pk>", catalog.PublishingDetail.as_view()),
    path("publishing_create/", catalog.PublishingCreate.as_view()),
    path("publishing_update/<int:pk>", catalog.PublishingUpdate.as_view()),
    path("publishing_delete/<int:pk>", catalog.PublishingDelete.as_view()),
    #BOOKS URLS
    path("book_list/", books.BookList.as_view()),
    path("book_detail/<int:pk>", books.BookDetail.as_view()),
    path("book_create/", books.BookCreate.as_view()),
    path("book_update/<int:pk>", books.BookUpdate.as_view()),
    path("book_delete/<int:pk>", books.BookDelete.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)