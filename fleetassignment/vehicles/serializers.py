from rest_framework import serializers

from fleetassignment.vehicles.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('model', 'full_name', 'plate_number')

class VehiclePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model =
