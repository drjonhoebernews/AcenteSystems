from rest_framework import serializers
from .models import TowTruck


class TowTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = TowTruck
        fields = '__all__'
