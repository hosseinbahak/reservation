from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueForYearValidator
import datetime
import django

class Room_numberSerializer(serializers.ModelSerializer):
    room_number = serializers.CharField()
    class Meta:
        fields = ('room_number', )
        model = Room

    def get_room_number(self, obj):
        return obj.room_number.room_number  


class ListBookedRoomsSerializer(serializers.Serializer):
    name = serializers.CharField()
    room_number = Room_numberSerializer()
    # we can add more features for getting more detail of room here
    room_information = room_number
    reserve_check_in = serializers.DateTimeField()
    reserve_check_out = serializers.DateTimeField()
    guests_count = serializers.IntegerField()


class ListAvailableRoomsSerializer(serializers.Serializer):
    room_number = serializers.IntegerField()


class ReserveRoomSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Reservation
        fields = ['id','reserve_check_in','reserve_check_out','name','room_number','guests_count']

    def get_room_number(self, obj):
        print(obj.room_number.room_number)

    def validate(self, obj):
        try:

            reserve = Reservation.objects.filter(room_number=obj['room_number'],
                                                reserve_check_out__gte = obj['reserve_check_in'], 
                                                reserve_check_in__lte = obj['reserve_check_out'])
            
            if reserve.values('reserved') :
                raise serializers.ValidationError("room is reserved at this time")

            if (obj['reserve_check_in'] > obj['reserve_check_out']):
                raise serializers.ValidationError("please insert reserve check in and reserve check out correctly")

            if  (obj['reserve_check_in'] < django.utils.timezone.now()):
                raise serializers.ValidationError("date and time are in invalid range")

            return obj

        except serializers.ValidationError as err:
            raise err
        except:
            raise serializers.ValidationError(
                "some thing went wrong on validation!")
