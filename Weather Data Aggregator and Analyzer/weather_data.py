import requests
from config import API_KEY, BASE_URL, LOCATION


def fetch_weather_data():
    params = {"q": LOCATION, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch data from API. Status Code: {response.status_code}")
        print("Response:", response.text)
        return None

    data = response.json()

    # Extract required weather data
    weather_info = {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": data["dt"],
    }

    print("Fetched Weather Data:", weather_info)

    return weather_info
