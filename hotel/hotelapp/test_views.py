from django.test import Client
from django.test import TestCase
from mixer.backend.django import mixer
from .models import BookingOrder
from faker import Faker
from usersapp.models import HotelUser


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    # На главную можно без регистрации
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Бронировать нельзя без регистрации
    def test_booking_no(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 302)

    # Бронировать  могут только зарегистрированные
    def test_booking_yes(self):
        HotelUser.objects.create_user(username='hotelier', email='redway@mail.ru', password='anapa2020')
        response = self.client.get('/booking/')
        # Без логина нельзя ...
        self.assertEqual(response.status_code, 302)

        # ... а с логином можно!
        self.client.login(username='hotelier', password='anapa2020')
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        HotelUser.objects.create_user(username='hotelier', email='redway@mail.ru', password='anapa2020')
        self.client.login(username='hotelier', password='anapa2020')
        # Есть первая страница
        response = self.client.get('/administration/?page=1')
        self.assertEqual(response.status_code, 200)
        # Нет десятой страницы
        response = self.client.get('/administration/?page=10')
        self.assertEqual(response.status_code, 404)

    def test_api(self):
        admin_user = HotelUser.objects.create_user(username='hotelier', email='redway@mail.ru',
                                                   password='anapa2020', is_superuser=True)
        self.assertTrue(admin_user.is_superuser)
        response = self.client.get('/api/v0/clients/')
        self.assertNotEqual(response.status_code, 200)  # надо зайти

        self.client.login(username='hotelier', password='anapa2020')

        response = self.client.get('/api/v0/clients/')  # зашли, теперь можно
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/api/v0/rooms/')  # только суперюзер
        self.assertEqual(response.status_code, 200)

        self.client.logout()

        # пробуем не суперюзера
        h_user = HotelUser.objects.create_user(username='ivanov', email='ivanov@m.ru', password='yj@y2mzaHb@6W9C')
        self.assertFalse(h_user.is_superuser)
        self.client.login(username='ivanov', password='yj@y2mzaHb@6W9C')

        response = self.client.get('/api/v0/rooms/')
        self.assertNotEqual(response.status_code, 200)  # только суперюзер

        response = self.client.get('/api/v0/clients/')  # а здесь любой
        self.assertEqual(response.status_code, 200)
