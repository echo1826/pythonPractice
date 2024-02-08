#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

spreadsheet_manager = DataManager()
search = FlightSearch()

sheet_data = spreadsheet_manager.get_rows()["prices"]
update = False

for row in sheet_data:
    if not row["iataCode"]:
        iata = search.get_iata(row["city"])
        row["iataCode"] = iata
        update = True
        
if update:
    spreadsheet_manager.update_sheet(sheet_data)
    
for row in sheet_data:
    flight_data = search.get_flights(row["iataCode"])
    if row["lowestPrice"] > flight_data.price:
        row["lowestPrice"] = flight_data.price
        spreadsheet_manager.update_price(row)