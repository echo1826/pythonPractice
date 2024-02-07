#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import urllib.parse

spreadsheet_manager = DataManager()
search = FlightSearch()

sheet_data = spreadsheet_manager.get_rows()["prices"]
update = False

for row in sheet_data:
    if not row["iataCode"]:
        iata = search.get_iata(row["city"])
        row["iataCode"] = iata
        update = True
        
print(sheet_data)
if update:
    spreadsheet_manager.update_sheet(sheet_data)