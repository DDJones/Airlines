from django.shortcuts import render
from serviceAirline.models import Flights, Cities,Airports,Reservations,Seats,Bookings,Passengers
from .serializers import flightsSerial, seatFareSearial,passengersSearialJSON
#import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from rest_framework.exceptions import APIException
import json
from datetime import datetime
from dateutil import parser

class ServiceUnavailable(APIException):
    status_code = 404
    default_detail = 'No matches.'
    default_code = 'service_unavailable'

# Create your views here.
@api_view(["GET"])
def flights(request):
    departure = None
    arrival = None
    flights = Flights.objects.all()
    if request.GET.get("departureAirportID"):
        departure = request.GET.get("departureAirportID")
        flights = flights.filter(DepartureAirportID__AirportName__contains=departure)
    if request.GET.get("arrivalAirport"):
        arrival = request.GET.get("arrivalAirport")
        flights = flights.filter(ArrivalAirportID__AirportName__contains=arrival)
    if request.GET.get("departureDate"):
        reqDate = request.GET.get("departureDate")
        reqParsed = parser.parse(reqDate)
        flights = flights.filter(DepartureDateTime__year=reqParsed.year,
                                 DepartureDateTime__month=reqParsed.month,
                                 DepartureDateTime__day=reqParsed.day)
    if request.GET.get("numPassengers"):
        reqNumber = int(request.GET.get("numPassengers"))
        for flight in flights:
            availible = flight.AvailibleSeats
            if availible < reqNumber:
                flights = flights.exclude(pk=flight.pk)
    
    serializer = flightsSerial(flights, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def options(request,flightId):
    flightSeats = Seats.objects.filter(FlightID=flightId,SeatStatus="A")
    serializer = seatFareSearial(flightSeats,many=True)
    return Response(serializer.data)
    
@api_view(["GET"])
def hold(request,flightId):
    unavail = ServiceUnavailable()
    if request.GET.get("numPassengers"):
        numPassengers = int(request.GET.get("numPassengers"))
    else:
        unavail.default_detail("numPassengers not specified")
        return Response(unavail)
    if request.GET.get("seatClassId"):
        seatClassId = int(request.GET.get("seatClassId"))
    else:
        unavail.default_detail("seatClassId not specified")
        return Response(unavail)
    
    flightSeats = Seats.objects.filter(FlightID=flightId,SeatStatus="A",ClassID=seatClassId)
    if numPassengers > flightSeats.count():
        unavail.default_detail("Not enough seats in this class")
        return Response(unavail)
    else:
        reservation = Reservations.objects.create(ReservationDate=datetime.now())
        for seat in flightSeats[:numPassengers]:
            seat.updateSeatStatus(status=seat.HOLD)
            seat.ReservationID = reservation
            seat.save()
            print(seat)
        return Response({"holdSuccessful":True,"holdId":reservation.pk})
    
@api_view(["POST"])    
def booking(request):
    data = request.data
    #passnger = passengersSearial(data["passengerDetails"][0])
    #print(passnger)
    print(request.data["passengerDetails"][0])
    return Response({"NICE":True})

