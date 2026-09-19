import requests
import os

def get_weather(city: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key or api_key.startswith("-"):
        return {"error": "OPENWEATHER_API_KEY is not configured or is invalid."}

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 404:
            return {"error": f"City '{city}' not found."}
        if response.status_code == 401:
            return {"error": "OpenWeatherMap authentication failed (401). Check OPENWEATHER_API_KEY."}

        response.raise_for_status()
        data = response.json()

        return {
            "city": city,
            "temperature": f"{data['main']['temp']} °C",
            "condition": data["weather"][0]["description"].capitalize(),
            "humidity": f"{data['main']['humidity']}%"
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather: {str(e)}"}

