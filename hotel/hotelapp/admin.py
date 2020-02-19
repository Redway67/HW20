from django.contrib import admin
from .models import Room, Client, BookingOrder, HistoryPrice

admin.site.register(Room)
admin.site.register(Client)
admin.site.register(BookingOrder)
admin.site.register(HistoryPrice)

