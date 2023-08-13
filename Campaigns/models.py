from django.db import models


class Campaign(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
