import requests
import json



body = {
    "numPassengers":118
}
r = requests.get("http://127.0.0.1:8000/api/flights",params=body)
print(r.text)

# body = {
#     "arrivalAirport":"LHR"
# }
# r = requests.get("http://sc19c2sw.pythonanywhere.com/api/flights",params=body)
# print(r.text