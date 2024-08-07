from django.urls import path
from . import views as catalog

app_name = "catalog"
urlpatterns = [
    #ATHOR URLS
    path("athor_list/", catalog.AthorList.as_view(), name="athor_list"),
    path("athor_detail/<int:pk>", catalog.AthorDetail.as_view(), name="athor_detail"),
    path("athor_create/", catalog.AthorCreate.as_view(), name="athor_create"),
    path("athor_update/<int:pk>", catalog.AthorUpdate.as_view(), name="athor_update"),
    path("athor_delete/<int:pk>", catalog.AthorDelete.as_view(), name="athor_delete"),
    #SERIA URLS
    path("seria_list/", catalog.SeriaList.as_view(), name="seria_list"),
    path("seria_detail/<int:pk>", catalog.SeriaDetail.as_view(), name="seria_detail"),
    path("seria_create/", catalog.SeriaCreate.as_view(), name="seria_create"),
    path("seria_update/<int:pk>", catalog.SeriaUpdate.as_view(), name="seria_update"),
    path("seria_delete/<int:pk>", catalog.SeriaDelete.as_view(), name="seria_delete"),
    #GENRE URLS
    path("genre_list/", catalog.GenreList.as_view(), name="genre_list"),
    path("genre_detail/<int:pk>", catalog.GenreDetail.as_view(), name="genre_detail"),
    path("genre_create/", catalog.GenreCreate.as_view(), name="genre_create"),
    path("genre_update/<int:pk>", catalog.GenreUpdate.as_view(), name="genre_update"),
    path("genre_delete/<int:pk>", catalog.GenreDelete.as_view(), name="genre_delete"),
    #PUBLISHING URLS
    path("publishing_list/", catalog.PublishingList.as_view(), name="publishing_list"),
    path("publishing_detail/<int:pk>", catalog.PublishingDetail.as_view(), name="publishing_detail"),
    path("publishing_create/", catalog.PublishingCreate.as_view(), name="publishing_create"),
    path("publishing_update/<int:pk>", catalog.PublishingUpdate.as_view(), name="publishing_update"),
    path("publishing_delete/<int:pk>", catalog.PublishingDelete.as_view(), name="publishing_delete"),
]