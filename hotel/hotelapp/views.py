from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from .models import Client, Gallery, BookingOrder
from usersapp.models import HotelUser
from .forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


class GalleryView(ListView):
    model = Gallery
    template_name = 'hotelapp/gallery.html'


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = BookingOrder
    fields = ['room', 'data_in', 'data_out', 'is_breakfast']
    success_url = reverse_lazy('hotel:index')
    template_name = 'hotelapp/booking.html'

    def form_valid(self, form):
        form.instance.who = self.request.user.client
        return super(BookingCreateView, self).form_valid(form)


class AdmListView(ListView):
    model = BookingOrder
    template_name = 'hotelapp/administration.html'
    context_object_name = 'books'
    paginate_by = 2

    def get_queryset(self):
        if self.request.user.is_superuser:
            return BookingOrder.objects.all()  # суперпользователь управляет всеми бронированиями
        else:
            return BookingOrder.objects.filter(who=self.request.user)


class BookDetailView(DetailView):
    model = BookingOrder
    fields = ['room', 'data_in', 'data_out', 'is_breakfast']
    template_name = 'hotelapp/booking_detail.html'
    success_url = reverse_lazy('hotel:administration')

    def get(self, request, *args, **kwargs):
        self.booking_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(BookingOrder, pk=self.booking_id)


class BookUpdateView(UpdateView):
    template_name = 'hotelapp/booking_update.html'
    model = BookingOrder
    fields = ['room', 'data_in', 'data_out', 'is_breakfast']
    success_url = reverse_lazy('hotel:administration')


class BookDeleteView(DeleteView):
    template_name = 'hotelapp/booking_delete_confirm.html'
    model = BookingOrder
    fields = ['room', 'data_in', 'data_out', 'is_breakfast']
    success_url = reverse_lazy('hotel:administration')
