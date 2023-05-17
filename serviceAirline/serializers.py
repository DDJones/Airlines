from rest_framework import serializers
from .models import Flights,Seats,Passengers



class flightsSerial(serializers.ModelSerializer):
    departureAirport = serializers.CharField(source='DepartureAirportID.AirportName')
    arrivalAirport = serializers.CharField(source='DestinationAirportID.AirportName')
    departureDateTime = serializers.DateTimeField(source ="DepartureDateTime")
    arrivalDateTime = serializers.DateTimeField(source = "ArrivalDateTime")
    availibleSeats = serializers.IntegerField(source = "AvailibleSeats")
    flightId = serializers.IntegerField(source ="pk")
    durationMins = serializers.IntegerField(source ="DurationMins")
    currency = serializers.CharField(source="Currency")
    class Meta:
        model = Flights
        fields = ["flightId","departureAirport","arrivalAirport","departureDateTime","arrivalDateTime"
                  ,"availibleSeats","durationMins","currency"]
        
class seatFareSearial(serializers.ModelSerializer):
    seatClassId = serializers.IntegerField(source= "ClassID.pk")
    className = serializers.CharField(source= "ClassID.Class")
    price= serializers.DecimalField(source= "SeatPrice",max_digits=10,decimal_places=2)
    class Meta:
        model = Seats
        fields =  ["seatClassId","className","price"]


class passengersSearialJSON(serializers.ModelSerializer):
    #Title = serializers.CharField(source = "Title")
    class Meta:

        model = Passengers
        alieses= {"Title":"title"}
        fields = ["Title"]
    




# class Passengers(models.Model):
#     Title = models.CharField(max_length=4,null=False)
#     First_Name = models.CharField(max_length=30,null=False)
#     Last_Name = models.CharField(max_length=30,null=False)
#     BookingID = models.ForeignKey(Bookings,null=True,on_delete=models.SET_NULL)
#     Seat = models.ForeignKey(Seats,on_delete=models.CASCADE)
#     PassportNumber = models.IntegerField()