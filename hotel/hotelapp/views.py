from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
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
    success_url = reverse_lazy('hotel:index')
    template_name = 'hotelapp/booking.html'


class WarningContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['warning'] = 'Это должно быть в отдельном приложении АРМ Администратора !'
        return context


class AdmListView(ListView, WarningContextMixin):
    model = BookingOrder
    template_name = 'hotelapp/administration.html'
    context_object_name = 'books'

    def get_queryset(self):
        return BookingOrder.objects.all()


class BookDetailView(DetailView, WarningContextMixin):
    model = BookingOrder
    template_name = 'hotelapp/booking_detail.html'
    success_url = reverse_lazy('hotel:administration')

    def get(self, request, *args, **kwargs):
        self.booking_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(BookingOrder, pk=self.booking_id)


class BookUpdateView(UpdateView, WarningContextMixin):
    template_name = 'hotelapp/booking_update.html'
    model = BookingOrder
    fields = '__all__'
    success_url = reverse_lazy('hotel:administration')


class BookDeleteView(DeleteView, WarningContextMixin):
    template_name = 'hotelapp/booking_delete_confirm.html'
    model = BookingOrder
    success_url = reverse_lazy('hotel:administration')
