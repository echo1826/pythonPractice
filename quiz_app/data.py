import requests

api_url = "https://opentdb.com/api.php"
params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(api_url, params=params)
response.raise_for_status()
data = response.json()
# print(data)

question_data = data["results"]
# print(question_data)