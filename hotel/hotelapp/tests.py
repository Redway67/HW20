from django.test import TestCase
from .models import Gallery, Room, Client, BookingOrder
from usersapp.models import HotelUser
from mixer.backend.django import mixer
from faker import Faker


# Create your tests here.
class GalleryTestCaseMixer(TestCase):

    def setUp(self):
        self.gallery = mixer.blend(Gallery)
        self.gallery_str = mixer.blend(Gallery, description='Какое-то описание')

    def test_has_image(self):
        print(f' Описание сгенерированное mixer: \n {self.gallery.description}')
        self.assertFalse(self.gallery.has_image())

    def test_str(self):
        self.assertEqual(str(self.gallery_str), 'Какое-то описание')


class BookingOrderTestCaseMixer(TestCase):

    def setUp(self):
        self.booking = mixer.blend(BookingOrder)
        # для тестирования суперюзера
        self.booking.who.password = 'anapa2020'
        self.booking.who.username = 'hotelier'

    def test_str(self):
        print('Бронирование:', self.booking)
        self.assertEqual(self.booking.who.username, 'hotelier')
