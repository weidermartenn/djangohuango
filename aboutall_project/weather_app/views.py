from django.shortcuts import render
import requests
import requests.exceptions
from .models import City

def weather(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=02586546b81e214ba2c5b751c986d399"

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        city_name = city.name
        try:
            city_weather = requests.get(url.format(city_name), timeout=5).json()
        except requests.exceptions.ReadTimeout:
            print('timeout')
            continue
        
        weather = {
            'city': city_name,
            'temperature': city_weather['main']['temp'],
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data}
    return render(request, './weather.html', context)
