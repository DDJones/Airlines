from django.db import models
import datetime

# Create your models here.


class Cities(models.Model):
    CityName = models.CharField(max_length=30, unique=True)
    def  __str__(self):
        return "{}".format(self.CityName)
    
class Airports(models.Model):
    AirportName = models.CharField(max_length=30,unique=True)
    CityID = models.ForeignKey(Cities,on_delete=models.CASCADE)
    def  __str__(self):
        return "{}".format(self.AirportName)

class Flights(models.Model):
    DepartureAirportID = models.ForeignKey(Airports,related_name="DepartureAirportID",on_delete=models.CASCADE)
    DestinationAirportID = models.ForeignKey(Airports,related_name="DestinationAirportID",on_delete=models.CASCADE)
    DepartureDateTime = models.DateTimeField(null=False)
    ArrivalDateTime = models.DateTimeField(null=False)
    AvailibleSeats = models.IntegerField(null=True)
    def updateAvailibleSeats(self):
        availible = Seats.objects.filter(FlightID=self.pk).filter(SeatStatus="A").count()
        self.AvailibleSeats = availible
        self.save()
        return availible
    def  __str__(self):
        return "{}: {}  TO {}: {}".format(self.DepartureAirportID.AirportName,self.DepartureDateTime,
                                          self.DestinationAirportID.AirportName,self.ArrivalDateTime)



class Reservations(models.Model):
    ReservationDate = models.DateTimeField(null=False)
    def  __str__(self):
        return "{}".format(self.ReservationDate)

class SeatClass(models.Model):
    Class = models.CharField(max_length=20,null=False)
    def  __str__(self):
        return "{}".format(self.Class)

class Seats(models.Model):
    AVAILIBLE = "A"
    RESERVED = "R"
    SEAT_STATUS_CHOICES=[(AVAILIBLE,"Availible"),(RESERVED,"Reserved")]
    FlightID = models.ForeignKey(Flights,on_delete=models.CASCADE)
    Row = models.CharField(max_length=2)
    SeatNumber = models.IntegerField()
    SeatStatus = models.CharField(max_length=10,choices=SEAT_STATUS_CHOICES)
    ReservationID = models.ForeignKey(Reservations,null=True ,on_delete=models.SET_NULL)
    ClassID = models.ForeignKey(SeatClass,related_name="ClassID",on_delete=models.CASCADE)
    SeatPrice = models.DecimalField(max_digits=10,decimal_places=2,null=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["FlightID", "Row","SeatNumber"], name='SeatPK'
            )
        ]
    def  __str__(self):
        return "{}{}{}  Status: {}   Class: {}  Price: {}".format(self.FlightID,self.Row,self.SeatNumber,
                                                       self.SeatStatus,self.ClassID,self.SeatPrice)

class Bookings(models.Model):
    FlightID = models.ForeignKey(Flights,on_delete=models.CASCADE)
    PaymentReference = models.CharField(max_length=100,null=False)
    def  __str__(self):
        return "FlightID: {}    Ref: {}".format(self.FlightID,self.PaymentReference)

class Passengers(models.Model):
    Title = models.CharField(max_length=4,null=False)
    First_Name = models.CharField(max_length=30,null=False)
    Last_Name = models.CharField(max_length=30,null=False)
    BookingID = models.ForeignKey(Bookings,null=True,on_delete=models.SET_NULL)
    Seat = models.ForeignKey(Seats,on_delete=models.CASCADE)
    PassportNumber = models.IntegerField()
    def  __str__(self):
        return "{} {}   BookingID: {}   Seat:{}".format(self.First_Name,self.Last_Name,self.BookingID,self.Seat)