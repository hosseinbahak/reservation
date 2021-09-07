from django.db import models


class Room(models.Model):
    room_number = models.CharField(max_length=100, unique=True)
    bed_count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (("room_number"),)


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.ForeignKey(Room, to_field='room_number', on_delete=models.CASCADE)
    reserve_check_in = models.DateTimeField()
    reserve_check_out = models.DateTimeField()
    guests_count = models.PositiveIntegerField(default=1)
    # this field help us to seprate empty rooms from reserved rooms
    reserved = models.BooleanField(default=True)


    def __str__(self):
        return  "room number: " +  self.room_number.room_number  + " reserved by: " + self.name + " from " + str(self.reserve_check_in) + " to " + str(self.reserve_check_out)

