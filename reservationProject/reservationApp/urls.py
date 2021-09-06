from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/booked_rooms/$', views.BookedRooms.as_view(), name='booked_rooms'),
    url(r'^api/available_rooms/$', views.AvailableRooms.as_view(), name='available_rooms'),
    url(r'^api/reserve_room/$', views.ReserveRoom.as_view(), name='reserve_room'),
    url(r'^api/room_info/$', views.RoomInfo.as_view(), name='Room_info'),
]