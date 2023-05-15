from django.shortcuts import render
from serviceAirline.models import Flights, Cities,Airports,Reservations,Seats,Bookings,Passengers
from .serializers import flightsSerial
#import requests
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import json
from datetime import datetime
# Create your views here.

def flights(request):
    departure = None
    arrival = None
    flights = Flights.objects.all()
    if request.GET.get("departureAirportID"):
        departure = request.GET.get("departureAirportID")
        flights = flights.filter(DepartureAirportID__AirportName__contains=departure)
        # for i in flights:
        #     print("NICE "+str(flights.DepartureAirportID))
    if request.GET.get("arrivalAirport"):
        arrival = request.GET.get("arrivalAirport")
        flights = flights.filter(ArrivalAirportID__AirportName__contains=arrival)

    if request.GET.get("numPassengers"):
        reqNumber = int(request.GET.get("numPassengers"))
        for flight in flights:
            availible = flight.AvailibleSeats
            print(flight.AvailibleSeats)
            
            if availible < reqNumber:
                print("YES")
                flights = flights.exclude(pk=flight.pk)
        print("DONE")
        print(flights)
    serializer = flightsSerial(flights, many=True)
    return JsonResponse(serializer.data,safe=False)




# def flights(request):
    # print(arrivalAirport)
    # http_bad_response = HttpResponseBadRequest()
    # http_bad_response["Content-Type"]= "text/plain"
    # # paramArrival = arrivalAirport
    # # print("AARRRIIVAL "+str(paramArrival))
    # if(request.method!="GET"):
    #     http_bad_response.content = "Only GET requests are allowed\n"
    #     return http_bad_response
    
    # flightList = Flights.objects.all()
    # the_list=[]
    # #seatList = Seats.objects.all()
    # for record in flightList:
    #     depTime = record.DepartureDateTime
    #     arrTime =record.ArrivalDateTime
    #     filterSeatList = Seats.objects.filter(FlightID=record.pk)
    #     item = {"departureAirport": record.DepartureAirportID.AirportName,
    #             "arrivalAirport": record.DestinationAirportID.AirportName,
    #             "departureDateTime": depTime.strftime("%Y-%m-%dT%H:%M:%S"),
    #             "arrivalDateTime": arrTime.strftime("%Y-%m-%dT%H:%M:%S"),
    #             "durationMins": (arrTime-depTime).total_seconds(),
    #             "minPrice": "{:.2f}".format(float(filterSeatList.order_by("SeatPrice")[0].SeatPrice)),
    #             "availableSeats": len(filterSeatList),
    #             "currency":"Sterling (GBP - £)"}
    #     the_list.append(item)
    # #payload = {"flight": the_list}
    # http_response = HttpResponse(json.dumps(the_list))
    # http_response["Content-Type"]= "application/json"
    # http_response.status_code = 200
    # http_response.reason_phrase = "OK"

    # return http_response