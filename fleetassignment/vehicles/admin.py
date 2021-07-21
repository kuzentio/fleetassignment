from django.contrib import admin

from fleetassignment.vehicles.models import Vehicle, VehiclePosition


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'model', 'plate_number')


@admin.register(VehiclePosition)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'lon', 'lat')
