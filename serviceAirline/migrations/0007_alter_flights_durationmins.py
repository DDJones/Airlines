# Generated by Django 4.2.1 on 2023-05-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceAirline', '0006_flights_durationmins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='DurationMins',
            field=models.IntegerField(null=True),
        ),
    ]
