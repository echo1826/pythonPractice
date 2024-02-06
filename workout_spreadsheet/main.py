import requests

APP_ID = "d95bd026"
API_KEY = "1b5adee7e5ccafd1efdff1244612eaf5"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_input = input("Tell me which exercises you did: ")

body = {
    "query": exercise_input
}

response = requests.post(url=exercise_endpoint, headers=headers, json=body)
response.raise_for_status()
print(response.json())

