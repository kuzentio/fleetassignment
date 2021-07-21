from rest_framework import viewsets

from fleetassignment.vehicles.models import Vehicle
from fleetassignment.vehicles.serializers import VehicleSerializer


class VehicleListViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self):
        qs = super(VehicleListViewSet, self).get_queryset()
        plate_number = self.request.query_params.get('plate_number')
        if plate_number is not None and isinstance(plate_number, int):
            qs = qs.filter(plate_number=plate_number)
        return qs


class VehiclePositionViewSet(viewsets.ModelViewSet):
    serializer_class = ''
