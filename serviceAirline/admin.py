from django.contrib import admin

# Register your models here.
from .models import Flights, Cities,Airports,Reservations,Seats,Bookings,Passengers

admin.site.register(Airports)
admin.site.register(Cities)
admin.site.register(Flights)
admin.site.register(Reservations)
admin.site.register(Seats)
admin.site.register(Bookings)
admin.site.register(Passengers)