from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.db.models import Q
from .serializers import *
from .models import *

class BookedRooms(APIView): 
    def get(self, request, format=None):
        pagination = PageNumberPagination()
        booked_rooms = Reservation.objects.filter(reserved=True)
        result_page = pagination.paginate_queryset(booked_rooms, request)
        serializer = ListBookedRoomsSerializer(result_page, many=True)
        data = paginate(serializer.data, pagination)
        return Response(data)


class RoomInfo(APIView): 
    def get(self, request, format=None):
        bookedRooms = Reservation.objects.filter(room_number_id=request.GET['room_number'])
        serializer = ListBookedRoomsSerializer(bookedRooms, many=True)
        return Response(serializer.data)


class ReserveRoom(APIView):
    def post(self, request, *args, **kwargs):
        updated_request = request.POST.copy()
        updated_request.update({'reserved': True})
        serializer = ReserveRoomSerializer(data=updated_request)
        serializer.is_valid(raise_exception=True)
        reserve = serializer.save()
        return Response(serializer.data)


def paginate(data, pagination):
    paginate_data = {
        'count': pagination.page.paginator.count,
        'next': pagination.get_next_link(),
        'previous': pagination.get_previous_link(),
        'results': data,
    }
    return paginate_data


class AvailableRooms(APIView): 
    def get(self, request, format=None):
        pagination = PageNumberPagination()
        #extract number of booked rooms(at a specific time) to find available rooms
        booked_rooms = Reservation.objects.filter(
            reserved = True,
            reserve_check_in = request.GET['reserve_check_in'], 
            reserve_check_out=request.GET['reserve_check_out'],
            ).values('room_number')
        
        #list of reserved rooms
        list_reserved_rooms=[]
        for i in range(0,len(booked_rooms)):
            list_reserved_rooms.append(booked_rooms[i]['room_number'])

        #list of empty rooms
        available_rooms = Room.objects.filter(~Q(room_number__in=list_reserved_rooms))

        result_page = pagination.paginate_queryset(available_rooms, request)
        serializer = ListAvailableRoomsSerializer(result_page, many=True)
        data = paginate(serializer.data, pagination)
        return Response(data)

def HomePage(request):
    booked_rooms = Reservation.objects.filter(reserved=True).order_by('reserve_check_in')
    return render(request, 'homepage.html', {'listings':booked_rooms})