STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from datetime import datetime

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api_key = "4D1B124ZGCSYOLGV"
news_api_key = "44a9b69abf6e44f9b3f96360447244fe"
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

day_before = 197.8600#float(last_two_days[0][1]['4. close'])
yesterday = 187.2900#float(last_two_days[1][1]['4. close'])
percentage_difference = ((yesterday - day_before) / day_before) * 100

if abs(percentage_difference) > 5:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    current_day = datetime.now().date()
    news_api = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": 'tesla',
        'language': 'en',
        'apiKey': news_api_key
    }
    response = requests.get(news_api, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    first_three_articles = news_data["articles"][:3]
    articles_to_send = []
    for news in first_three_articles:
        articles_to_send.append((news['title'], news['description']))
        
    print(articles_to_send)
