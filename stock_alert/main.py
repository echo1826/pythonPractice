STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api_key = "4D1B124ZGCSYOLGV"
stock_api = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

# response = requests.get(stock_api, params=stock_parameters, timeout=10)
# response.raise_for_status()
# stock_data = response.json()

# last_two_days = list(stock_data["Time Series (Daily)"].items())[1:3]

# print(last_two_days[0])
# print(last_two_days[1])
day_before = 197.8600#float(last_two_days[0][1]['4. close'])
yesterday = 187.2900#float(last_two_days[1][1]['4. close'])
percentage_difference = ((yesterday - day_before) / day_before) * 100
print(percentage_difference)

if percentage_difference > 5 or percentage_difference < -5:
    print("get news")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    
