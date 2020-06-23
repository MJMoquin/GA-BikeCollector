from django.db import models
from django.urls import reverse

class Bike(models.Model):
    bike_brand = models.CharField(max_length=50)
    bike_model = models.CharField(max_length=50)
    production_year = models.IntegerField()
    terrain_type = models.CharField(max_length=20)

    def __str__(self):
        return self.bike_model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bike_id': self.id})
    