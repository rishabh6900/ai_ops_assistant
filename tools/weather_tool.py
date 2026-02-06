import requests
import os

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
