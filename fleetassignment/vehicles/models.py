from django.db import models


class Vehicle(models.Model):
    full_name = models.CharField(max_length=255, blank=False)
    plate_number = models.PositiveIntegerField()
    model = models.CharField(max_length=255, blank=False)


class VehiclePosition(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    lon = models.FloatField()
    lat = models.FloatField()

    mpoly = models.MultiPolygonField()
