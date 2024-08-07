from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

class LoginUser(LoginView):
    template_name = "login.html"
