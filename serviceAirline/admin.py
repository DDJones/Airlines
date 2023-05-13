from django.contrib import admin

# Register your models here.
from .models import Airports, Cities, Flights

admin.site.register(Airports)
admin.site.register(Cities)
admin.site.register(Flights)