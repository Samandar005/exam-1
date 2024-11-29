from django.db import models

class Meal(models.Model):
    meal_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.PositiveIntegerField()
    type = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=100)
