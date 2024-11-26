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

from user import views as user_app
from books import views as books
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", books.MainView.as_view(), name="main"),
    path("login/", user_app.LoginUser.as_view(), name='login'),
    path("logout/", user_app.LogoutView.as_view(), name='logout'),
    path('password_change', user_app.PasswordChangeView.as_view(), name ='password_change'),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("books/", include("books.urls", namespace ="books")),
    path("accounts/", include("accounts.urls", namespace ="accounts")),
    path("orders/", include("orders.urls", namespace ="orders")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)