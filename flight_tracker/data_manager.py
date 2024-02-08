import requests
from flight_data import FlightData

ENDPOINT = "https://api.sheety.co/eb2523f79e0755f83c584c6c0f685727/flightDeals/prices"
headers = {
    "Authorization": "Bearer gkajwgepauiohspodubpawe"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass
        
    def get_rows(self):
        response = requests.get(url=ENDPOINT, headers=headers)
        return response.json()
    
    def update_sheet(self, update_value):
        for row in update_value:
            
            body = {
                "price": row
            }
            res = requests.put(url=f"{ENDPOINT}/{body['price']['id']}", headers=headers, json=body)
            print(res.status_code)
            
    def update_price(self, row):
        
        res = requests.put(url=f"{ENDPOINT}/{row['id']}", headers=headers, json={"price":row})
        print(res.text)

