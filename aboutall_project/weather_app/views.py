from django.shortcuts import render
import requests
import requests.exceptions
from .models import City
from datetime import datetime, timedelta

def weather_visual(description):
    weather_icbg = {
        'Sunny': '../static/assets/icon-sun.svg',
        'Clear': '../static/assets/icon-clear.svg',
        'Partly Cloudy': '../static/assets/icon-partcloud.svg',
        'Light rain': '../static/assets/icon-lightrain.svg',
        'Patchy rain nearby': '../static/assets/icon-lightrainsun.svg',
        'Overcast': '../static/assets/icon-overcast.svg',
        'Mist': '../static/assets/icon-mist.svg',
    }   

    if description in weather_icbg:
        return weather_icbg[description]

def weather(request):
    API_KEY = 'd0c69695c93247ebbee83252240410'

    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        if city_name:
            url = 'https://api.weatherapi.com/v1/current.json?key={}&q={}'
            try:
                response = requests.get(url.format(API_KEY, city_name)).json()
                data = response

                description = data['current']['condition']['text']
                print(description)
                weather_desc = weather_visual(description)

                weather_data = {
                    'time': (data['location']['localtime']).split(' ')[1],
                    'region': (data['location']['country']),
                    'city': (data['location']['name']),
                    'temperature': round(data['current']['temp_c']),
                    'feels_like': round(data['current']['feelslike_c']),
                    'wind_speed': round(data['current']['wind_mph']),
                    'humidity': round(data['current']['humidity']),
                    'pressure': round(data['current']['pressure_mb']),
                    'weather_icon': weather_desc,
                }
            except UnboundLocalError as e:
                print("Error fetching weather data: {}".format(str(e)))
                weather_data = None
            except requests.exceptions.RequestException:
                print("Ошибка запроса")
                weather_data = None
            
        else:
            print("Please enter a city name.")
    else:
        return render(request, './weather.html')

    return render(request, './weather.html', {'weather_data': weather_data})