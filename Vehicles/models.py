from django.db import models


class Vehicle(models.Model):
    VEHICLE_TYPES = [
        # Araç türleri için detaylandırma yapılabilir.
    ]
    FUEL_TYPES = [
        # Yakıt türleri için detaylandırma yapılabilir.
    ]
    type = models.CharField(choices=VEHICLE_TYPES, max_length=20)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    production_year = models.IntegerField()
    fuel_type = models.CharField(choices=FUEL_TYPES, max_length=20)
    engine_power = models.DecimalField(max_digits=5, decimal_places=2)
    mileage = models.IntegerField()
    has_damage = models.BooleanField(default=False)
    accident_history = models.TextField(blank=True)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    modifications = models.TextField(blank=True)
    usage_purpose = models.TextField()
    parking_situation = models.TextField()
