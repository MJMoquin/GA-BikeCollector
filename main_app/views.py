from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bike

def home(request):
  return render(request, 'home.html')

def bikes_index(request):
  bikes = Bike.objects.all()
  return render(request, 'bikes/index.html', {'bikes': bikes})

def bikes_detail(request, bike_id):
  bike = Bike.objects.get(id=bike_id)
  return render(request, 'bikes/detail.html', { 'bike': bike })

class BikeCreate(CreateView):
  model = Bike
  fields = '__all__'

class BikeUpdate(UpdateView):
  model = Bike
  fields = '__all__'

class BikeDelete(DeleteView):
  model = Bike
  success_url = '/bikes/'