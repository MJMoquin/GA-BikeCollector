from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bike, Equipment
from .forms import RideForm

def home(request):
  return render(request, 'home.html')

def bikes_index(request):
  bikes = Bike.objects.all()
  return render(request, 'bikes/index.html', {'bikes': bikes})

def bikes_detail(request, bike_id):
  bike = Bike.objects.get(id=bike_id)
  ride_form = RideForm()
  return render(request, 'bikes/detail.html', { 'bike': bike, 'ride_form': ride_form })

class BikeCreate(CreateView):
  model = Bike
  fields = '__all__'

class BikeUpdate(UpdateView):
  model = Bike
  fields = '__all__'

class BikeDelete(DeleteView):
  model = Bike
  success_url = '/bikes/'

def add_ride(request, bike_id):
  form = RideForm(request.POST)
  if form.is_valid():
    new_ride = form.save(commit=False)
    new_ride.bike_id = bike_id
    new_ride.save()
  return redirect('detail', bike_id=bike_id)

class EquipmentList(ListView):
  model = Equipment

class EquipmentDetail(DetailView):
  model = Equipment

class EquipmentCreate(CreateView):
  model = Equipment
  fields = '__all__'

class EquipmentUpdate(UpdateView):
  model = Equipment
  fields = ['equipment_type', 'brand']

class EquipmentDelete(DeleteView):
  model = Equipment
  success_url = '/equipment/'