from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
from datetime import datetime

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def get_weatherforecast(request):
    if request.method == 'POST':
        location = request.POST['location']

        api_key = 'P5GVQ7FYR7Z92XHPXKT2UQ48G'  # Replace with your Visual Crossing API key
        api_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}"

        # Query Parameters
        params = {
            "key": api_key,
            "unitGroup": "us",  # Choose the unit group (us, metric, etc.)
            "contentType": "json",  # Response content type (json, csv, etc.)
        }

        # Making the API request
        response = requests.get(api_url.format(location=location), params=params)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse and extract weather data from the JSON response
            weather_data = response.json()

            # Extract forecast data
            forecast_days = weather_data.get('days', [])

            # Process forecast data as needed
            forecast_list = []
            for day in forecast_days:
                forecast_list.append({
                    'date': datetime.utcfromtimestamp(day['datetime']/1000).strftime('%Y-%m-%d'),
                    'temperature_max': day.get('temp2m_max', ''),
                    'temperature_min': day.get('temp2m_min', ''),
                    'precipitation': day.get('precip', ''),
                    'wind_speed': day.get('wspd10m', ''),
                    'wind_direction': day.get('wdir10m', ''),
                    'humidity': day.get('humidity', ''),
                    'pressure': day.get('sealevelpressure', ''),
                    'visibility': day.get('visibility', ''),
                    'cloud_cover': day.get('cloudcover', ''),
                })

            return render(request, 'forecast.html', {'forecast_list': forecast_list})

        else:
            # Print an error message if the request was not successful
            return render(request, 'error.html', {'error_message': f"Error: {response.status_code} - {response.text}"})

    return render(request, 'index.html')
