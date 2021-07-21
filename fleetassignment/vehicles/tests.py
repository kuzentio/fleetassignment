from django.test import TestCase
from django_dynamic_fixture import G
from rest_framework.reverse import reverse

from fleetassignment.vehicles.models import Vehicle


class VehicleTestCase(TestCase):
    def test_vehicle_list_view(self):
        for i in range(5):
            G(Vehicle, plate_number=1)
        response = self.client.get(reverse('api:vehicles-list'))
        import ipdb; ipdb.set_trace()
