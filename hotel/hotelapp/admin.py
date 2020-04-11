from django.contrib import admin
from .models import Room, Client, BookingOrder, HistoryPrice, Gallery


def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'type', 'is_active']
    actions = [set_active]


admin.site.register( Room, RoomAdmin)
admin.site.register(Client)
admin.site.register(BookingOrder)
admin.site.register(HistoryPrice)
admin.site.register(Gallery)
