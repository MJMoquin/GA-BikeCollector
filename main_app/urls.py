from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bikes/', views.bikes_index, name='index'),
    path('bikes/<int:bike_id>/', views.bikes_detail, name='detail'),
    path('bikes/create/', views.BikeCreate.as_view(), name='bike_create'),
    path('bikes/<int:pk>/update/', views.BikeUpdate.as_view(), name='bike_update'),
    path('bikes/<int:pk>/delete/', views.BikeDelete.as_view(), name='bike_delete'),
]
