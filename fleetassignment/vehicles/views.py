from rest_framework import viewsets

from fleetassignment.vehicles.models import Vehicle, VehiclePosition
from fleetassignment.vehicles.serializers import VehicleSerializer, VehiclePositionSerializer


class VehicleListViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def process_search_location(self, queryset):
        start_lat = self.request.query_params.get('lat')
        start_lon = self.request.query_params.get('lon')
        # TODO: not implemented ^^

    def get_queryset(self):
        qs = super(VehicleListViewSet, self).get_queryset()
        plate_number = self.request.query_params.get('plate_number')
        if plate_number is not None and isinstance(plate_number, int):
            qs = qs.filter(plate_number=plate_number)

        nearby_radius = self.request.query_params.get('nearby_radius')
        if nearby_radius is not None:
            self.process_search_location(qs)

        return qs


class VehiclePositionViewSet(viewsets.ModelViewSet):
    queryset = VehiclePosition.objects.all()
    serializer_class = VehiclePositionSerializer
