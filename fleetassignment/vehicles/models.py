from django.core.cache import cache
from django.db import models


class Vehicle(models.Model):
    full_name = models.CharField(max_length=255, blank=False)
    plate_number = models.PositiveIntegerField()
    model = models.CharField(max_length=255, blank=False)


class VehiclePosition(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    lon = models.FloatField()
    lat = models.FloatField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None) -> None:
        super().save()
        if self.pk:
            cache.set(
                f'{self.vehicle.id}::latest',
                {'lon': self.lon, 'lat': self.lat, 'id': self.id},
            )
