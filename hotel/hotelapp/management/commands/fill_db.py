from django.core.management.base import BaseCommand, CommandError
from hotelapp.models import Room, Client, BookingOrder, HistoryPrice


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Работаем!!')
