from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import HotelUser
from hotelapp.models import Client


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'


class UserCreateView(CreateView):
    model = Client
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')

