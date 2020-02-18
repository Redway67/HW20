from django.contrib import admin
from .models import Rooms, Clients, BookingOrders

admin.site.register(Rooms)
admin.site.register(Clients)
admin.site.register(BookingOrders)

