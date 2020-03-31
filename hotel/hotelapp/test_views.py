from django.test import Client
from django.test import TestCase
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
