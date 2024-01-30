import requests # package used to fetch an api
from datetime import datetime

LAT = 30.267153
LONG = -97.743057

# # response coming back is an object that contains information about the response we got back
# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# # print(response.status_code)

# # can have the response raise the exception for us if a bad response comes back
# response.raise_for_status() # this method will raise an exception if we have a bad response

# data = response.json()
# print(data)

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

current_time = datetime.now()
sunrise = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
print(current_time.hour)
