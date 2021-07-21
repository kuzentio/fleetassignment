from django.contrib import admin

from fleetassignment.vehicles.models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'model', 'plate_number')
