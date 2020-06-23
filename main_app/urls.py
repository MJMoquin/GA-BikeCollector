from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bikes/', views.bikes_index, name='index'),
    path('bikes/<int:bike_id>/', views.bikes_detail, name='detail'),
]
