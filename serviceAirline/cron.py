import django
from django.utils import timezone
from serviceAirline.models import Flights, Cities,Airports,Reservations,Seats,Bookings,Passengers,SeatClass
import json
import datetime
import random
def my_scheduled_job():
  now = datetime.datetime.now()
  reservation = Reservations.objects.filter(ReservationDate__lt=now-datetime.timedelta(minutes=2))
  for res in reservation:
    seats = Seats.objects.filter(ReservationID=res.pk)
    if seats[0].SeatStatus == "R":
      pass
    elif seats[0].SeatStatus == "H":
      for seat in seats:
        seat.SeatStatus = "A"
        seat.save()
      
