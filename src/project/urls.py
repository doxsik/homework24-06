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
from django.urls import path, include
from django.conf.urls.static import static
from testapp import views as testapp
from catalog import views as catalog
from books import views as books
from user import views as user_app
from django.contrib.auth.views import LoginView, LogoutView
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", testapp.home_page),
    path("login/", user_app.LoginUser.as_view(), name='login'),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("books/", include("books.urls", namespace ="books")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)