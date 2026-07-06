from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AccommodationViewSet

router = DefaultRouter()
router.register("", AccommodationViewSet, basename="accommodations")

urlpatterns = [
    path("", include(router.urls)),
]