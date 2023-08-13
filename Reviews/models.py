from django.db import models
from Users.models import CustomUser
from Towtrucks.models import TowTruck


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="reviews_given")
    towtruck = models.ForeignKey(TowTruck, on_delete=models.CASCADE, related_name="reviews_received")
    comment = models.TextField()
    rating = models.PositiveIntegerField()
