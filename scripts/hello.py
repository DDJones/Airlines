import django
from serviceAirline.models import Flights, Cities,Airports,Reservations,SeatClass,Seats,Bookings,Passengers
import json
import datetime
import random
def hello():
    f = open('Airline.json')
    data = json.load(f)
    idx = 0
    unique = { each['flightId'] : each for each in data }.values()
    print(len(unique))
    for i in unique:
        # if i["from_municipality"] == "0" or i["to_municipality"] == "0":
        #     pass
        # depcity = Cities.objects.create(CityName = i["from_municipality"])
        # arrcity = Cities.objects.create(CityName = i["to_municipality"])
        idx+=1
        if idx==5:
            break
    f.close()
    return()

def make_small():
    city = ["Brussels","Glasgow","Paris","Duesseldorf","Florence","Berlin"]
    airport = ["BRU","GLA","PAR","DUS","FLR","BER"]
    rowChar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
               'P','Q','R','S','T','U','V','W','X','Y','Z']
    businessClass = ["A","B","C","D","E"]
    timehours = [1,4,3]
    for i in range (3):
        cfrom = Cities.objects.create(CityName = city[i])
        afrom = Airports.objects.create(AirportName = airport[i],CityID=cfrom)

        cto = Cities.objects.create(CityName = city[i+3])
        ato = Airports.objects.create(AirportName = airport[i+3],CityID=cto)
        date = datetime.datetime(2023,8,1,12,4,5)
        flight = Flights.objects.create(DepartureAirportID = afrom,DestinationAirportID=ato,
                                        DepartureDateTime =date,ArrivalDateTime=date+datetime.timedelta(hours=timehours[i]))
        for row in rowChar:
            for column in range (6):
                column+=1
                ran = random.randint(1,10)%3
                if ran == 0:
                    status = "R"
                else:
                    status = "A"
                if row in businessClass:
                    seatClass = "Business Class"
                else:
                    seatClass = "Economy Class"
                seat = Seats.objects.create(FlightID=flight,Row=row,SeatNumber=column,
                                            SeatStatus=status)


    print("NICE")


def run():
    make_small()