from django.shortcuts import render
from serviceAirline.models import Flights, Cities,Airports,Reservations,Seats,Bookings,Passengers
#import requests
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import json

# Create your views here.

def flights(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response["Content-Type"]= "text/plain"

    if(request.method!="GET"):
        http_bad_response.content = "Only GET requests are allowed\n"
        return http_bad_response
    
    flightList = Flights.objects.all()
    the_list=[]

    for record in flightList:
        depTime = record.DepartureDateTime.strftime("%Y-%m-%dT%H:%M:%S")
        arrTime =record.ArrivalDateTime.strftime("%Y-%m-%dT%H:%M:%S")
        item = {"departureAirport": record.DepartureAirportID.AirportName,
                "arrivalAirport": record.DestinationAirportID.AirportName,
                "departureDateTime": depTime,
                "arrivalDateTime": arrTime}
        the_list.append(item)
    #payload = {"flight": the_list}
    http_response = HttpResponse(json.dumps(the_list))
    http_response["Content-Type"]= "application/json"
    http_response.status_code = 200
    http_response.reason_phrase = "OK"

    return http_response