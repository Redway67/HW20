from django.core.management.base import BaseCommand, CommandError
from hotelapp.models import Room, Gallery, HistoryPrice

PATH_PIC = '/gallery/'


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


        Gallery.objects.create(image=PATH_PIC + 'beach.jpg', description='Пляж "Кавказ"')
        Gallery.objects.create(image=PATH_PIC + 'pioneer_prospect.jpg', description='Пионерский проспект')
        Gallery.objects.create(image=PATH_PIC + 'naberezhnaya-anapyi.jpg', description='Набережная Анапы')
        Gallery.objects.create(image=PATH_PIC + 'redsquare.jpg', description='Торговый комплекс "Красная Площадь"')
        print('Заполнение фотогалереи')

        HistoryPrice.objects.create(data='2020-01-01', price=1000.00)
        print('Заполнены цена за номер с 01 января')
