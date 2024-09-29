from django.shortcuts import render
import requests
import requests.exceptions
from .models import City
from datetime import datetime, timedelta

weather_icons = {
    'Clear': '/assets/icon-sun.svg',
    'Clouds': './assets/icon-clouds.svg',
    'Rain': './assets/icon-rain.svg',
}

def weather(request):
    LANG = 'ru'
    UNITS = 'metric'
    API_KEY = '02586546b81e214ba2c5b751c986d399'

    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        print(city_name)
        if city_name:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&lang={}&appid={}'
            try:
                response = requests.get(url.format(city_name, UNITS, LANG, API_KEY)).json()
                data = response
                weather_data = {
                    'city': data['name'],
                    'temperature': round(data['main']['temp']),
                    'feels_like': round(data['main']['feels_like']),
                    'min_temp': round(data['main']['temp_min']),
                    'max_temp': round(data['main']['temp_max']),
                    'wind_speed': data['wind']['speed'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'weather_icon': weather_icons.get(data['weather'][0]['main']),
                }
            except requests.exceptions.RequestException as e:
                print("Error fetching weather data: {}".format(str(e)))
        else:
            print("Please enter a city name.")
    else:
        return render(request, './weather.html')

    return render(request, './weather.html', {'weather_data': weather_data})