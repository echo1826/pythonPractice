import requests
import os

env_api_key = os.environ.get("OWM_API_KEY") # how to load environment variables from the machine
LAT = 30.267153
LONG = -97.743057
weather_api = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "appid": env_api_key,
    "lat": LAT,
    "lon": LONG,
    "units": "imperial",
    "cnt": 4
}

response = requests.get(weather_api, params=parameters)
response.raise_for_status()
data = response.json()

# print(data["list"][0]["weather"][0]["id"])

for forecast in data["list"]:
    condition_code = forecast["weather"][0]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an Umbrella")