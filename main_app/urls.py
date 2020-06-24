from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bikes/', views.bikes_index, name='index'),
    path('bikes/<int:bike_id>/', views.bikes_detail, name='detail'),
    path('bikes/create/', views.BikeCreate.as_view(), name='bike_create'),
    path('bikes/<int:pk>/update/', views.BikeUpdate.as_view(), name='bike_update'),
    path('bikes/<int:pk>/delete/', views.BikeDelete.as_view(), name='bike_delete'),
    path('bikes/<int:bike_id>/add_ride/', views.add_ride, name='add_ride'),
    path('equipment/', views.EquipmentList.as_view(), name='equipment_index'),
    path('equipment/<int:pk>/', views.EquipmentDetail.as_view(), name='equipment_detail'),
    path('equipment/create/', views.EquipmentCreate.as_view(), name='equipment_create'),
    path('equipment/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipment_update'),
    path('equipment/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipment_delete'),
]
