from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'reserve_check_in', 'reserve_check_out', 'name', 'get_room_number', 'guests_count', 'reserved',]

    def get_room_number(self, obj):
        return obj.room_number.room_number

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id','room_number','bed_count',]