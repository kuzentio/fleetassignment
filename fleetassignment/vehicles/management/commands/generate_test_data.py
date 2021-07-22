import random

from django.contrib.gis.geos import GEOSGeometry
from django.core.management import BaseCommand
from django_dynamic_fixture import G

from fleetassignment.vehicles.models import Vehicle, VehiclePosition


class Command(BaseCommand):
    help = "This command is responsible for generating fake Vehicles data"

    def handle(self, *args, **options):
        for plate in range(3):
            for vehicle in range(random.randint(1, 50)):
                _vehicle = G(Vehicle, plate_number=plate)
                for position in range(random.randint(1, 10)):
                    lat = random.uniform(10.00, 1000.00)
                    lon = random.uniform(10.00, 1000.00)
                    G(
                        VehiclePosition,
                        vehicle=_vehicle,
                        lat=lat,
                        lon=lon,
                        point=GEOSGeometry(f'POINT({lat} {lon})')
                    )
