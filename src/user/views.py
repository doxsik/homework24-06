from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.urls import reverse_lazy

class LoginUser(LoginView):
    template_name = "login.html"
    

class LogoutUser(LogoutView):
    template_name = None


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"