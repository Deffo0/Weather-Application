from django.shortcuts import render

# Create your views here.

import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' 
        + city + '&units=metric&appid=208094a1951842871c040004ada05c36').read()
        list_of_data = json.loads(source)
        data = {
            "city" : str(city),
            "country_code" : str(list_of_data['sys']['country']),
            "coordinate" : str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp']) + '°C',
            "pressure" : str(list_of_data['main']['pressure']) + 'hPa',
            "humidity" : str(list_of_data['main']['humidity']) + '%',
            "main" : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : str(list_of_data['weather'][0]['icon']),

        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)