import requests
from datetime import datetime

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

exercise_response = requests.post(url=exercise_endpoint, headers=headers, json=body)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()['exercises']
# print(exercise_data)

sheety_post_endpoint = "https://api.sheety.co/eb2523f79e0755f83c584c6c0f685727/myWorkoutsPythonPractice/workouts"
sheety_headers = {
    "Authorization": "Bearer tiwqyuergakjhfwbsdaoi"
}


for exercise in exercise_data:
    current_date = datetime.now().strftime("%d/%m/%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    sheety_body = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheety_response = requests.post(url=sheety_post_endpoint, json=sheety_body, headers=sheety_headers)
    sheety_response.raise_for_status()
    print(sheety_response.json())