from urllib.error import HTTPError
from django.shortcuts import render
from decouple import config
import urllib
import json


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST["city"]

        api_key = config("WEATHER_API_KEY")

        try:
            res = urllib.request.urlopen(
                "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric")

            json_data = json.loads(res.read().decode('utf-8'))

            data = {
                "country_code": str(json_data["sys"]["country"]),
                "coordinate": "Latitude:"+str(json_data["coord"]["lat"]) + ", " + "Longitude:"+str(json_data["coord"]["lat"]),
                "temperature": str(json_data["main"]["temp"]),
                "pressure": str(json_data["main"]["pressure"]),
                "humidity": str(json_data["main"]["humidity"]),
                "windspeed": str(json_data["wind"]["speed"]),
            }
        except HTTPError as err:
            if err.code == 404:
                data = {"error": f'"{city}" not found'}
            else:
                data = {"error": "Could not get weather data, try again later."}
        except Exception as err:
            data = {"error": "Something went wrong, try again later."}
    else:
        city = ""
        data = {}
    return render(request, "index.html", {"city": city, "data": data})
