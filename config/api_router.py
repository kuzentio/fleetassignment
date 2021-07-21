from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from fleetassignment.vehicles.views import VehicleListViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("vehicles", VehicleListViewSet)


app_name = "api"
urlpatterns = router.urls
