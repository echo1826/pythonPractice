import requests

ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
CITY_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
API_KEY = "IPGkOsejWrOPGIHjEzuvqJkxPmDPp9Gp"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
    
    def get_iata(self, city_name):
        params = {
            "term": city_name
        }
        response = requests.get(url=CITY_ENDPOINT, headers={"apikey": API_KEY}, params=params)
        response.raise_for_status()
        data = response.json()
        return data["locations"][0]["code"]