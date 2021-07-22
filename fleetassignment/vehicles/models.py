from django.core.cache import cache
from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import GEOSGeometry


class Vehicle(models.Model):
    full_name = models.CharField(max_length=255, blank=False)
    plate_number = models.PositiveIntegerField()
    model = models.CharField(max_length=255, blank=False)


class VehiclePosition(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    lon = models.FloatField()
    lat = models.FloatField()
    point = PointField(srid=32140, blank=True, null=True)

    def save(self, *args, **kwargs) -> None:
        self.point = GEOSGeometry(f'POINT({self.lat} {self.lon})')
        super().save()
        if self.pk:
            cache.set(
                f'{self.vehicle.id}::latest',
                {'lon': self.lon, 'lat': self.lat, 'id': self.vehicle.id},
            )
