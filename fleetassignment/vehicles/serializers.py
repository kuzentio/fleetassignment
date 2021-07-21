from django.core.cache import cache
from rest_framework import serializers

from fleetassignment.vehicles.models import Vehicle, VehiclePosition


class VehicleSerializer(serializers.ModelSerializer):
    last_position = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = ('id', 'model', 'full_name', 'plate_number', 'last_position')

    def get_last_position(self, obj):
        latest_cache_point = cache.get(f"{obj.id}::latest")
        if not latest_cache_point:
            return VehiclePositionSerializer(obj.vehicleposition_set.last()).data
        return VehiclePositionSerializer(
            obj.vehicleposition_set.get(id=latest_cache_point['id'])
        ).data


class VehiclePositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehiclePosition
        fields = ('lon', 'lat', 'vehicle')
