import requests
from flight_data import FlightData

ENDPOINT = "https://api.sheety.co/eb2523f79e0755f83c584c6c0f685727/flightDeals/prices"
headers = {
    "Authorization": "Bearer gkajwgepauiohspodubpawe"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        response = requests.get(url=ENDPOINT, headers=headers)
        data = FlightData(response.json())
        self.data = data.get_iata()
        
    def populate_iata(self):
        for row in self.data["prices"]:
            body = {
                "price": row
            }
            res = requests.put(url=f"{ENDPOINT}/{body['price']['id']}", headers=headers, json=body)
            print(res.text)

data = DataManager()
data.populate_iata()