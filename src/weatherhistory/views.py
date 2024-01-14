from django.shortcuts import render

# Create your views here.
# weather_/views.py

@csrf_exempt
def get_weatherhistory(request):
    if request.method == 'POST':
        location = request.POST['location']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        # Additional parameters
        # Add more parameters as needed based on your requirements

        # Replace 'YOUR_API_KEY' with your Visual Crossing Weather API key
        api_key = 'YOUR_API_KEY'
        api_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history'

        # Additional query parameters for historical weather
        params = {
            'aggregateHours': 24,
            'unitGroup': 'uk',
            'contentType': 'json',
            'dayStartTime': '0:0:00',
            'dayEndTime': '0:0:00',
            'location': location,
            'startDateTime': start_date,
            'endDateTime': end_date,
            'key': api_key,
            # Include additional parameters here
        }

        # Making the API request
        response = requests.get(api_url, params=params)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse and extract historical weather data from the JSON response
            history_data = response.json()

            # Process historical weather data as needed
            # Extract required information from history_data dictionary

            return render(request, 'weatherhistory.html', {'history_data': history_data})

        else:
            # Print an error message if the request was not successful
            return render(request, 'error.html', {'error_message': f"Error: {response.status_code} - {response.text}"})

    return render(request, 'index.html')
