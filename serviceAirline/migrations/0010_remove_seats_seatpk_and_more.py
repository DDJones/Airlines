# Generated by Django 4.2.1 on 2023-05-17 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceAirline', '0009_flights_airline'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='seats',
            name='SeatPK',
        ),
        migrations.RenameField(
            model_name='airports',
            old_name='AirportName',
            new_name='airportName',
        ),
        migrations.RenameField(
            model_name='airports',
            old_name='CityID',
            new_name='cityID',
        ),
        migrations.RenameField(
            model_name='bookings',
            old_name='FlightID',
            new_name='flightID',
        ),
        migrations.RenameField(
            model_name='bookings',
            old_name='PaymentReference',
            new_name='paymentReference',
        ),
        migrations.RenameField(
            model_name='cities',
            old_name='CityName',
            new_name='cityName',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='Airline',
            new_name='airline',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='ArrivalDateTime',
            new_name='arrivalDateTime',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='AvailibleSeats',
            new_name='availibleSeats',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='Currency',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='DepartureAirportID',
            new_name='departureAirportID',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='DepartureDateTime',
            new_name='departureDateTime',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='DestinationAirportID',
            new_name='destinationAirportID',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='DurationMins',
            new_name='durationMins',
        ),
        migrations.RenameField(
            model_name='passengers',
            old_name='BookingID',
            new_name='bookingID',
        ),
        migrations.RenameField(
            model_name='passengers',
            old_name='First_Name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='passengers',
            old_name='Last_Name',
            new_name='lastName',
        ),
        migrations.RenameField(
            model_name='passengers',
            old_name='PassportNumber',
            new_name='passportNumber',
        ),
        migrations.RenameField(
            model_name='passengers',
            old_name='Seat',
            new_name='seat',
        ),
        migrations.RenameField(
            model_name='passengers',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='reservations',
            old_name='ReservationDate',
            new_name='reservationDate',
        ),
        migrations.RenameField(
            model_name='seatclass',
            old_name='Class',
            new_name='className',
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='ClassID',
            new_name='classID',
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='Currency',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='FlightID',
            new_name='flightID',
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='ReservationID',
            new_name='reservationID',
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='Row',
            new_name='row',
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='SeatNumber',
            new_name='seatNumber',
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='SeatPrice',
            new_name='seatPrice',
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='SeatStatus',
            new_name='seatStatus',
        ),
        migrations.AddConstraint(
            model_name='seats',
            constraint=models.UniqueConstraint(fields=('flightID', 'row', 'seatNumber'), name='SeatPK'),
        ),
    ]
