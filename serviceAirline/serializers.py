from rest_framework import serializers
from .models import Flights,Seats



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
