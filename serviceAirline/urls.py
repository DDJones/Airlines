from django.urls import path

from . import views

urlpatterns = [
    path("flights/", views.flights, name="flights"),
    # path("flights/<int:DepartureAirportID>",views.flightArr, name="flightsArr")
    path("flights/<int:flightId>/options",views.options,name="options")
]