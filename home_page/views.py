from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from . import request_weather


def home_page(request):
    context ={

    }
    return render(request, 'home_page/index.html', context=context)


def weather_page(request):
    context = {
        "weather": request_weather.request_get_weather()
    }
    return render(request, 'home_page/weather.html', context=context)
