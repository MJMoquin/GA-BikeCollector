from django.db import models

class Bike(models.Model):
    bike_brand = models.CharField(max_length=50)
    bike_model = models.CharField(max_length=50)
    production_year = models.IntegerField()
    terrain_type = models.CharField(max_length=20)