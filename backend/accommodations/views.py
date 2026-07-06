from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Accommodation
from .serializers import AccommodationSerializer


class AccommodationViewSet(viewsets.ModelViewSet):

    serializer_class = AccommodationSerializer

    def get_queryset(self):
        queryset = Accommodation.objects.all()

        trip = self.request.query_params.get("trip")

        if trip:
            queryset = queryset.filter(trip_id=trip)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
