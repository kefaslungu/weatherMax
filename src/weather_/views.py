from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import requests
from datetime import datetime

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def get_weather(request):
    if request.method == 'POST':
        location = request.POST['location']

        # Replace 'YOUR_API_KEY' with your Weatherstack API key
        api_key = 'b5c29e8545969de1bc4a997ea4edeaff'
        url = f'http://api.weatherstack.com/current?access_key={api_key}&query={location}'

        response = requests.get(url)
        data = response.json()

        # Extract weather data from the JSON response
        weather_data = {
            'location': location,
            'time': data['current']['observation_time'],
            'temperature': data['current']['temperature'],
            'precipitation': data['current']['precip'],
            'wind_speed': data['current']['wind_speed'],
            'wind_direction': data['current']['wind_dir'],
            'humidity': data['current']['humidity'],
            'pressure': data['current']['pressure'],
            'visibility': data['current']['visibility'],
            'cloud_cover': data['current']['cloudcover'],
        }

        return render(request, 'weather.html', {'weather_data': weather_data})

    return render(request, 'index.html')
