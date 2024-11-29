from django.db import models

class Driver(models.Model):
    taxi_name = models.CharField(max_length = 100)
    license_plate = models.PositiveIntegerField()
    driver_name = models.CharField(max_length=100)
    passenger_capacity = models.PositiveIntegerField()
    car_model = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
