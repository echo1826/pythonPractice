import requests

ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
API_KEY = "IPGkOsejWrOPGIHjEzuvqJkxPmDPp9Gp"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        pass
    
    def get_iata(self, city_name):
        response = requests.get(url=ENDPOINT, params={"term": city_name}, headers={"apikey": API_KEY})
        data = response.json()
        return data["locations"][0]["code"]