from django.db import models
from Users.models import CustomUser
from Vehicles.models import Vehicle


class Policy(models.Model):
    POLICY_TYPES = [
        # Poliçe türleri için detaylandırma yapılabilir.
    ]
    agency = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="agency_policies")
    subagency = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="subagency_policies", null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_policies")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    policy_type = models.CharField(choices=POLICY_TYPES, max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)
