from django.db import models
from phone_field import PhoneField
from usersapp.models import HotelUser


class ActiveManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)


class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


# Номерной фонд
# Поле is_active. Номер может быть выведен из обращения: ремонт, спецбронирование, не сезон и т.д.
class Room(IsActiveMixin):
    number = models.PositiveSmallIntegerField()
    TYPE_CHOICES = (
        ('D', 'Одна двуспальная кровать'),
        ('S', 'Две односпальные кровати'),
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    def __str__(self):
        return f' {self.number} {self.type}'


# Клиенты
class Client(HotelUser):
    family_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday = models.DateField()
    live_place = models.CharField(max_length=30)
    phone = PhoneField(blank=True)
    passport = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.family_name} {self.name}'


# hotelier anapa2020
# ivanov yj@y2mzaHb@6W9C
# petrov Xa9cur47@bunZMb

# Бронирования
class BookingOrder(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    who = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    data_in = models.DateField(db_index=True)
    data_out = models.DateField()
    is_breakfast = models.BooleanField()

    def __str__(self):
        return f'Гость:{self.who.name} Заезд:{self.data_in} Выезд:{self.data_out} Номер:{self.room}'


# Прайс
class HistoryPrice(models.Model):
    data = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.data} {self.price}'


class Gallery(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery', null=True, blank=True)
    description = models.TextField(blank=True)

    def has_image(self):
        return bool(self.image)

    def __str__(self):
        return f'{self.description}'
