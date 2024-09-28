from django.shortcuts import render
import requests
import requests.exceptions
from .models import City

weather_icons = {
    'Clear' : '/assets/icon-sun.svg',
    'Clouds' : './assets/icon-clouds.svg',
    'Rain' : './assets/icon-rain.svg',
}

# def weather(request):
#     API_KEY = '02586546b81e214ba2c5b751c986d399'
#     url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}"

    
#     return render(request, './weather.html')

def weather(request):
    return render(request, './weather.html')