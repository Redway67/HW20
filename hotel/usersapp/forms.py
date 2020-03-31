from django.contrib.auth.forms import UserCreationForm
from hotelapp.models import Client


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = (
            'username', 'password1', 'password2', 'email', 'family_name', 'name', 'birthday', 'passport', 'live_place',
            'phone')