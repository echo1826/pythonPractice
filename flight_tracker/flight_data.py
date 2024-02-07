import requests

ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
API_KEY = "IPGkOsejWrOPGIHjEzuvqJkxPmDPp9Gp"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, spreadsheet):
        self.spreadsheet = spreadsheet
    
    
    def get_iata(self):
        for row in self.spreadsheet["prices"]:
            if not row["iataCode"]:
                params = {
                    "term": row["city"],
                    "locale": "en-US"
                }
                response = requests.get(url=ENDPOINT, params=params, headers={"apikey": API_KEY})
                data = response.json()
                print(data["locations"][0]["code"])
                row["iataCode"] = data["locations"][0]["code"]
        return self.spreadsheet