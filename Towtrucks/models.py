from django.db import models
from Users.models import CustomUser


class TowTruck(models.Model):
    STATUS = [
        ('AVAILABLE', 'Available'),
        ('BUSY', 'Busy')
    ]
    agency = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="towtrucks")
    location = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS, max_length=10)
