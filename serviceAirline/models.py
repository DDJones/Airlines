from django.db import models
import datetime

# Create your models here.

class Cities(models.Model):
    CityID = models.IntegerField(primary_key=True)
    CityName = models.CharField(max_length=30)

class Airports(models.Model):
    AirportID = models.IntegerField(primary_key=True)
    AirportName = models.CharField(max_length=30)
    CityID = models.ForeignKey(Cities,on_delete=models.DO_NOTHING)

class Flights(models.Model):
    FlightID = models.IntegerField(primary_key=True)
    DepartureAirportID = models.ForeignKey(Airports,related_name="DepartureAirportID",on_delete=models.DO_NOTHING)
    DestinationAirportID = models.ForeignKey(Airports,related_name="DestinationAirportID",on_delete=models.DO_NOTHING)
    ArrivalDateTime = models.DateTimeField(null=False)
    ArrivalDateTime = models.DateTimeField(null=False)