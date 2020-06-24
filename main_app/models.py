from django.db import models
from django.urls import reverse
from datetime import date

class Equipment(models.Model):
  equipment_type = models.CharField(max_length=50)
  brand = models.CharField(max_length=20)

  def __str__(self):
    return self.equipment_type

  def get_absolute_url(self):
    return reverse('equipment_detail', kwargs={'pk': self.id})

class Bike(models.Model):
    bike_brand = models.CharField(max_length=20)
    bike_model = models.CharField(max_length=50)
    production_year = models.IntegerField()
    terrain_type = models.CharField(max_length=20)

    equipment = models.ManyToManyField(Equipment)

    def __str__(self):
        return self.bike_model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bike_id': self.id})
    

class Ride(models.Model):
    date = models.DateField()
    duration = models.IntegerField()

    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.duration} minute ride on {self.date}"

    class Meta:
        ordering = ['-date']

