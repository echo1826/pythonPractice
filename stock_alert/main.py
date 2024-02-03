STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from datetime import datetime
from datetime import timedelta
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api_key = "4D1B124ZGCSYOLGV"
stock_api = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

response = requests.get(stock_api, params=stock_parameters, timeout=10)
response.raise_for_status()
stock_data = response.json()
# print(stock_data["Time Series (Daily)"])
current_date = str(datetime.now().date())
yesterday_date = str(datetime.now().date() - timedelta(days=1))
print(stock_data["Time Series (Daily)"][current_date])
print(stock_data["Time Series (Daily)"][yesterday_date])
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

