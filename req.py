import requests
import json


def posting():
    details = {
    "title":"Mr",
    "firstName":"John",
    "lastName":"Smith",
    "passportNumber":"02319093",
    "dateOfBirth":"2000-6-23"
    }
 
    flightDetails = {
        "airline":"British Airways",
        "flightId":1,
        "departureAirport":"BRU",
        "arrivalAirport":"DUS",
        "departureDateTime":"2023-08-01",
        "arrivalDateTime":"2023-08-01",
        "durationMins":60,
        "price":50.00,
        "currency":"GBP",
        "seatClass":"Economy"
    }
    passengerDetails = []
    passengerDetails.append(details)
    body = {
        "seatClassId":2,
        "passengerDetails":passengerDetails,
        "flightDetails":flightDetails
        }

    r = requests.post("http://127.0.0.1:8000/api/booking", json=body)
    print(r.text)


def flights():
    r = requests.get("http://127.0.0.1:8000/api/flights")
    print(r.text)


def book():
    body = {
        "numPassengers":5,
        "seatClassId":2
    }
    r = requests.get("http://127.0.0.1:8000/api/flights/1/hold",params=body)
    print(r.text)


flights()