from django.shortcuts import render
from serviceAirline.models import Flights, Cities,Airports,Reservations,Seats,Bookings,Passengers
from .serializers import flightsSerial, seatFareSearial,passengersSearial
#import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import json
from datetime import datetime
from dateutil import parser
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
        #print(dateti.month)
        flights = flights.filter(DepartureDateTime__year=reqParsed.year,
                                 DepartureDateTime__month=reqParsed.month,
                                 DepartureDateTime__day=reqParsed.day)
    if request.GET.get("numPassengers"):
        reqNumber = int(request.GET.get("numPassengers"))
        for flight in flights:
            availible = flight.AvailibleSeats
            print(flight.AvailibleSeats)
            if availible < reqNumber:
                flights = flights.exclude(pk=flight.pk)
        print(flights)
    
    serializer = flightsSerial(flights, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def options(request,flightId):
    flightSeats = Seats.objects.filter(FlightID=flightId,SeatStatus="A")
    serializer = seatFareSearial(flightSeats,many=True)
    return Response(serializer.data)
    
@api_view(["GET"])
def hold(request,flightId):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response["Content-Type"]= "text/plain"
    if request.GET.get("numPassengers"):
        numPassengers = int(request.GET.get("numPassengers"))
    else:
        http_bad_response.reason_phrase= "numPassengers not specified"
        return http_bad_response
    if request.GET.get("seatClassId"):
        seatClassId = int(request.GET.get("seatClassId"))
    else:
        http_bad_response.reason_phrase = "seatClassId not specified"
        return http_bad_response
    
    flightSeats = Seats.objects.filter(FlightID=flightId,SeatStatus="A",ClassID=seatClassId)
    if numPassengers > flightSeats.count():
        failed = JsonResponse({"holdSuccessful":False})
        failed.reason_phrase = "Not enough seats in this class"
        failed.status_code = 404
        return failed
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
    print(request.data["passengerDetails"][0]["title"])
    # if "flightDetails" in request.POST:
    #     print("NICE")
    # if request.POST.get("passengerDetails"):
    #     passengerDetails = request.POST.get("passengerDetails")
    #     print("GOOD\n")
    #     print(passengerDetails[0])
    # if request.GET.get("flightDetails"):
    #     flightDetails = request.GET.get("flightDetails")
    #     print("GOODNUMVER2\n")
    #     print(flightDetails)
    # if request.GET.get("seatClassId"):
    #     seatClassId = request.GET.get("seatClassId")
    #     print("GOODNUMVER2\n")
    #     print(seatClassId   )
    return Response({"NICE":True})

