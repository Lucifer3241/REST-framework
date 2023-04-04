from django.db import models

# Create your models here.


class Airport(models.Model):
    AirportName=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)

    def __str__(self):
        return self.AirportName