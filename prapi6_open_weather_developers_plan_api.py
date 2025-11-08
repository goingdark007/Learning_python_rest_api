import requests
from dotenv import dotenv_values

config = dotenv_values('.env')

API_KEY = config['API_KEY']
LAT, LON = 23.8103, 90.4125

def get_weather_data():
    # URLs
    current_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units=metric&appid={API_KEY}"
    hourly_url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={LAT}&lon={LON}&units=metric&appid={API_KEY}"
    daily_url = f"https://pro.openweathermap.org/data/2.5/forecast/daily?lat={LAT}&lon={LON}&cnt=7&units=metric&appid={API_KEY}"

    # Fetch data
    current_data = requests.get(current_url).json()
    hourly_data = requests.get(hourly_url).json()
    daily_data = requests.get(daily_url).json()

    # Merge logically
    merged_data = {
        "location": current_data.get("name", ""),
        "coordinates": {
            "lat": LAT,
            "lon": LON
        },
        "current": current_data,
        "hourly": hourly_data,
        "daily": daily_data.get("list", [])
    }

    return merged_data

data = get_weather_data()

# print(data["location"])
# print("Current Temp:", data["current"]["main"]["temp"])
# print("Next hour forecast count:", len(data["hourly"]))
# print("Next 7 days forecast count:", len(data["daily"]))
print(f'hourly: {data["hourly"]}')
