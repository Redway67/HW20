from django.core.management.base import BaseCommand, CommandError
from hotelapp.models import Room, Client, BookingOrder, HistoryPrice


class Command(BaseCommand):

    def handle(self, *args, **options):

        print('Работаем MVT')
        Room.objects.create(number=101, type='D')
        Room.objects.create(number=102, type='S')
        Room.objects.create(number=103, type='D')
        Room.objects.create(number=201, type='S')
        Room.objects.create(number=202, type='D')
        Room.objects.create(number=203, type='S')
        print('Заполнены номера гостиницы')

        HistoryPrice.objects.create(data='2020-01-01', price=1000.00)
        print('Заполнены цена за номер с 01 января')

