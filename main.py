import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 190
AGE = 46

APP_ID = "5f23e95b"
API_KEY = "xxxxxxxxxxxxxx"


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
googlesheet_endpoint = "https://api.sheety.co/xxxxxxxxx/workoutTracking/workouts"


exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
 }



response = requests.post(nutritionix_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


# https://api.sheety.co/76ba36480fe6783ed7ebb3a1970666a9/workoutTracking/workouts

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    print(sheet_inputs)

    sheet_response = requests.post(googlesheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)