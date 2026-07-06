from django.urls import include, path

urlpatterns = [
    path("trips/", include("trips.urls")),
    path("accommodations/", include("accommodations.urls")),
]
