import requests
from datetime import datetime, timedelta
from flight_data import FlightData

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
    
    def get_flights(self, destination_code):
        tomorrow = datetime.now() + timedelta(1)
        six_months = tomorrow + timedelta(days=182.5)

        # for row in sheet_data:
        params = {
            "fly_from": "LAX",
            "fly_to": destination_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "curr": "USD",
            "one_for_city": 1,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0
        }
        res = requests.get(url=ENDPOINT, headers={"apikey": API_KEY}, params=params)
        try:
            data = res.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_code}")
            
        flight_data = FlightData(price=data["price"], origin_city=data["cityFrom"], origin_airport=data["flyFrom"], destination_city=data["cityTo"], destination_airport=data["flyTo"], out_date=data["route"][0]["local_departure"].split("T")[0], return_date=data["route"][0]["local_departure"].split("T")[1])
        return flight_data