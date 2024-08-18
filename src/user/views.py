from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

class LoginUser(LoginView):
    template_name = "login.html"
    

class LogoutUser(LogoutView):
    template_name = None