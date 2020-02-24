from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Client
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def main_view(request):
    clients = Client.objects.all()
    return render(request, 'hotelapp/index.html', context={'clients': clients})


def create_post(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из форы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail(
                'Contact message',
                f'Ваш сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect(reverse('hotel:index'))
        else:
            return render(request, 'hotelapp/create.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'hotelapp/create.html', context={'form': form})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'hotelapp/post.html', context={'post': post})