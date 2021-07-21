from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from fleetassignment.vehicles.views import VehicleListViewSet, VehiclePositionViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("vehicles", VehicleListViewSet)
router.register("vehicle-position", VehiclePositionViewSet)


app_name = "api"
urlpatterns = router.urls
