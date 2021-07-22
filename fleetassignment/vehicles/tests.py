from django.test import TestCase
from django.core.cache import cache
from django_dynamic_fixture import G
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED

from fleetassignment.vehicles.models import Vehicle, VehiclePosition


class VehicleTestCase(TestCase):
    def test_vehicle_list_view(self):
        for i in range(5):
            G(Vehicle, plate_number=1)
        response = self.client.get(reverse('api:vehicle-list'))
        vehicles = response.json()
        self.assertEqual(len(vehicles), Vehicle.objects.all().count())

    def test_posting_vehicle_position_saves_position_in_cache(self):
        vehicle = G(Vehicle, plate_number=1)
        vehicle_position = G(VehiclePosition, vehicle=vehicle, lat=30.00, lon=15.00)
        vehicle_position.save()
        self.assertIsNotNone(cache.get(f"{vehicle.id}::latest"))

    def test_vehicle_position_goes_to_cache(self):
        vehicle = G(Vehicle, plate_number=1)
        response = self.client.post(
            reverse('api:vehicleposition-list'), data={'vehicle': vehicle.id, 'lat': 10.00, 'lon': 10.00}
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertIsNotNone(cache.get(f"{vehicle.id}::latest"))

    def test_only_latest_vehicle_position_goes_to_cache(self):
        vehicle = G(Vehicle, plate_number=1)
        G(VehiclePosition, vehicle=vehicle, lat=30.00, lon=15.00)
        cached_value = cache.get(f"{vehicle.id}::latest")
        self.assertIsNotNone(cached_value)
        self.assertEqual(cached_value['lat'], 30.00)
        response = self.client.post(
            reverse('api:vehicleposition-list'), data={'vehicle': vehicle.id, 'lat': 10.00, 'lon': 10.00}
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        cached_value = cache.get(f"{vehicle.id}::latest")
        self.assertEqual(cached_value['lat'], 10.00)

    def test_searching_vehicles_from_redis(self):
        vehicle1 = G(Vehicle, plate_number=1)
        vehicle2 = G(Vehicle, plate_number=2)
        test_pos = G(VehiclePosition, vehicle=vehicle1, lat=30.088, lon=15.088)
        G(VehiclePosition, vehicle=vehicle2, lat=3000.00, lon=1500.00)
        url = reverse('api:vehicle-list') + '?nearby_radius=90000&lon=15.088&lat=30.088'
        response = self.client.get(url)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], test_pos.vehicle.id)
