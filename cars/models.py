from django.db import models

class CarDetail(models.Model):
    brand = models.CharField(max_length=255)  # Brand of the car
    model = models.CharField(max_length=255)  # Model name
    accel_sec = models.FloatField()  # Acceleration in seconds (0-100 km/h)
    top_speed_kmh = models.IntegerField()  # Top speed in km/h
    range_km = models.IntegerField()  # Range in km
    efficiency_whkm = models.IntegerField()  # Efficiency in Wh/km
    fast_charge_kmh = models.IntegerField()  # Fast charging speed in km/h
    rapid_charge = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])  # Rapid charging availability
    powertrain = models.CharField(max_length=255)  # Powertrain (AWD, FWD, etc.)
    plug_type = models.CharField(max_length=255)  # Plug type
    body_style = models.CharField(max_length=255)  # Body style (Sedan, SUV, etc.)
    segment = models.CharField(max_length=255)  # Market segment
    seats = models.IntegerField()  # Number of seats
    price_euro = models.FloatField()  # Price in euros before tax incentives

    def __str__(self):
        return f"{self.brand} {self.model}"
