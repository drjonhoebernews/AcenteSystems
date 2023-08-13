from rest_framework import generics
from .models import TowTruck
from .serializers import TowTruckSerializer


class TowTruckListView(generics.ListCreateAPIView):
    queryset = TowTruck.objects.all()
    serializer_class = TowTruckSerializer


class TowTruckDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TowTruck.objects.all()
    serializer_class = TowTruckSerializer
