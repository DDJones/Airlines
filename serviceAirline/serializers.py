from rest_framework import serializers
from .models import Flights



class flightsSerial(serializers.ModelSerializer):
    departureAirportID = serializers.CharField(source='DepartureAirportID.AirportName')
    destinationAirportID = serializers.CharField(source='DestinationAirportID.AirportName')
    departureDateTime = serializers.DateTimeField(source ="DepartureDateTime")
    availibleSeats = serializers.IntegerField(source = "AvailibleSeats")
    class Meta:
        model = Flights
        fields = ["departureAirportID","destinationAirportID","departureDateTime","availibleSeats"]