from django.db import models
import datetime

# Create your models here.


class Cities(models.Model):
    CityName = models.CharField(max_length=30, unique=True)

class Airports(models.Model):
    AirportName = models.CharField(max_length=30,unique=True)
    CityID = models.ForeignKey(Cities,on_delete=models.CASCADE)

class Flights(models.Model):
    DepartureAirportID = models.ForeignKey(Airports,related_name="DepartureAirportID",on_delete=models.CASCADE)
    DestinationAirportID = models.ForeignKey(Airports,related_name="DestinationAirportID",on_delete=models.CASCADE)
    DepartureDateTime = models.DateTimeField(null=False)
    ArrivalDateTime = models.DateTimeField(null=False)



class Reservations(models.Model):
    ReservationDate = models.DateTimeField(null=False)

class SeatClass(models.Model):
    Class = models.CharField(max_length=20,null=False)

class Seats(models.Model):
    AVAILIBLE = "A"
    RESERVED = "R"
    SEAT_STATUS_CHOICES=[(AVAILIBLE,"Availible"),(RESERVED,"Reserved")]
    FlightID = models.ForeignKey(Flights,on_delete=models.CASCADE)
    Row = models.CharField(max_length=2)
    SeatNumber = models.IntegerField()
    SeatStatus = models.CharField(max_length=10,choices=SEAT_STATUS_CHOICES)
    ReservationID = models.ForeignKey(Reservations,null=True ,on_delete=models.SET_NULL)
    ClassID = models.ForeignKey(SeatClass,null=False,on_delete=models.CASCADE)
    SeatPrice = models.IntegerField(null=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["FlightID", "Row","SeatNumber"], name='SeatPK'
            )
        ]

class Bookings(models.Model):
    FlightID = models.ForeignKey(Flights,on_delete=models.CASCADE)
    PaymentReference = models.CharField(max_length=100,null=False)

class Passengers(models.Model):
    Title = models.CharField(max_length=4,null=False)
    First_Name = models.CharField(max_length=30,null=False)
    Last_Name = models.CharField(max_length=30,null=False)
    BookingID = models.ForeignKey(Bookings,null=True,on_delete=models.SET_NULL)
    Seat = models.ForeignKey(Seats,on_delete=models.CASCADE)
    PassportNumber = models.IntegerField()