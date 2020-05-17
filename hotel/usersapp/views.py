from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse

from .forms import RegistrationForm
from django.views.generic import CreateView, DetailView
from .models import HotelUser
from hotelapp.models import Client

from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from rest_framework.authtoken.models import Token


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'


class UserCreateView(CreateView):
    model = Client
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')


class UserDetailView(DetailView):
    model = Client
    template_name = 'usersapp/profile.html'


def update_token(request):
    user = request.user
    # если уже есть
    if hasattr(user, 'auth_token'):
        # обновить
        user.auth_token.delete()
        Token.objects.create(user=user)
    else:
        # создать
        Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))

