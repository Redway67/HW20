from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from .models import Client, Gallery, BookingOrder
from .forms import ContactForm


# Главная страница - описание, пока ничего не меняем
def main_view(request):
    return render(request, 'hotelapp/index.html', context={})


# Сообщения оставим как есть, потому что не храним в базе.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail(
                'Contact message',
                f'Ваше сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('hotel:index'))
        else:
            return render(request, 'hotelapp/contact.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'hotelapp/contact.html', context={'form': form})


# Все остальное переписываем на CBV
class GalleryView(ListView):
    model = Gallery
    template_name = 'hotelapp/gallery.html'


class BookingCreateView(CreateView):
    model = BookingOrder
    fields = '__all__'
    exclude = ('room',)  # Номер комнаты вводит Администратор
    success_url = reverse_lazy('hotel:index')
    template_name = 'hotelapp/booking.html'


class AdmListView(ListView):
    model = BookingOrder
    template_name = 'hotelapp/administration.html'
