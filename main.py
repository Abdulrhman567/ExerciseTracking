import requests
from datetime import datetime
import os

TOKEN = os.environ.get("TOKEN")
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

GENDER = None # Put your Gende here
WEIHGT_KG = None # Put your weight here
HEIGHT_CM = None # Put your heihgt here
AGE = None # Put your age here

exercise_endpoint = os.environ.get("EXERCISE_ENDPOINT")
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

# The exercise date
exercise_text = input("What exercise you did today?! ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

exercise_data = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 90.0,
    "height_cm": 180,
    "age": 25,
}

response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
data = response.json()

# Display it on the sheet 
today = datetime.now()
exercise_date = today.strftime("%d/%m/%Y")
exercise_time = today.strftime("%H:%M:%S")

for exercise in data['exercises']:
    row_data = {
        'workout': {
            'date': exercise_date,
            'time': exercise_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

response = requests.post(url=sheet_endpoint, json=row_data, headers=bearer_headers)
