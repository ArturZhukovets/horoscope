from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('weather/', views.weather_page, name='weather'),

]