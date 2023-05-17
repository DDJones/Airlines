import django
from django.utils import timezone
from serviceAirline.models import Flights, Cities,Airports,Reservations,Seats,Bookings,Passengers,SeatClass
import json
import datetime
import random

def populate():
    rowChar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
               'P','Q','R','S','T','U','V','W','X','Y','Z']
    firstClass = ["A","B","C","D","E"]
    businessClass =['F','G','H','I','J','K']
    airlines = ["Virgin","EasyJet","British Airways","United"]
    first = SeatClass.objects.create(Class="First Class")
    business = SeatClass.objects.create(Class="Business Class")
    economy = SeatClass.objects.create(Class="Economy")
    f = open('Airline.json')
    data = json.load(f)
    idx = 0
    # unique = { each['flightId'] : each for each in data }.values()
    # print(len(unique))
    for i in data:
        try:
            if i["from_municipality"] == "0" or i["to_municipality"] == "0":
                pass
            try:
                cityfromJSON = Cities.objects.get(CityName=str(i["from_municipality"]))
            except Cities.DoesNotExist:
                cityfromJSON = Cities.objects.create(CityName=str(i["from_municipality"]))
            try:
                citytoJSON = Cities.objects.get(CityName=str(i["to_municipality"]))
            except Cities.DoesNotExist:
                citytoJSON = Cities.objects.create(CityName=str(i["to_municipality"]))
            
            try:
                airportfromJSON = Airports.objects.get(AirportName=str(i["from_airportcode"]))
            except Airports.DoesNotExist:
                airportfromJSON = Airports.objects.create(AirportName=str(i["from_airportcode"]),CityID=cityfromJSON)
            try:
                airporttoJSON = Airports.objects.get(AirportName=str(i["to_airportcode"]))
            except Airports.DoesNotExist:
                airporttoJSON = Airports.objects.create(AirportName=str(i["to_airportcode"]),CityID=citytoJSON)
            
            date = datetime.datetime.strptime(i["departureDateTime"],"%Y-%m-%d %H:%M:%S")
            arrdate = datetime.datetime.strptime(i["arrivalDateTime"],"%Y-%m-%d %H:%M:%S")
            duration = i["durationMins"]

            flight = Flights.objects.create(Airline=random.choice(airlines),DepartureAirportID = airportfromJSON,
                                            DestinationAirportID=airporttoJSON,
                                            DepartureDateTime =date,ArrivalDateTime=arrdate,Currency="GBP",
                                            DurationMins=duration)
            
            for row in rowChar:
                for column in range (6):
                    column+=1
                    ran = random.randint(1,10)%3
                    if ran == 0:
                        status = "R"
                    else:
                        status = "A"
                    if row in firstClass:
                        seatClass = first
                        seatPrice = (duration*3)+50
                    elif row in businessClass:
                        seatClass = business
                        seatPrice = (duration*2)+20
                    else:
                        seatClass = economy
                        seatPrice = (duration*1)
                    seat = Seats.objects.create(FlightID=flight,Row=row,SeatNumber=column,
                                                SeatStatus=status,ClassID = seatClass,SeatPrice= seatPrice,Currency="GBP")
            flight.updateAvailibleSeats()
            
        except KeyError:
            pass

        idx+=1
        print("\nIDX="+str(idx))
    f.close()


def run():
    populate()