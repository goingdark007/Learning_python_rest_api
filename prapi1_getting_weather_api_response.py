import requests

url = "https://api.open-meteo.com/v1/forecast"

""" Adding query to get the data we need"""
params = {
	"latitude": 23.7104,
	"longitude": 90.4074,
	"daily": ["weather_code", "precipitation_probability_max", "temperature_2m_max", "temperature_2m_min"],
	"hourly": ["temperature_2m", "weather_code"],
	"current": ["temperature_2m", "relative_humidity_2m", "precipitation", "weather_code", "wind_speed_10m", "wind_direction_10m", "apparent_temperature", "is_day"],
	"timezone": "auto",
}
try:
    # Gets the response from the api using the params query
    responses = requests.get(url, params=params)

    # If api there's no error status code returns 200
    if responses.status_code == 200:
        # Converting the response to json
        data = responses.json()

        # Process first location. Add a for-loop for multiple locations or weather models
        print(f"Coordinates: {data['latitude']}°N {data['longitude']}°E")
        print(f"Elevation: {data['elevation']} m asl")
        print(f"Timezone: {data['timezone']}{data['timezone_abbreviation']}")
        print(f"Timezone difference to GMT+0: {data['utc_offset_seconds']}s")

        # Process current data. The order of variables needs to be the same as requested
        # Getting only the current weather dictionary from the json
        current_data = data['current']
        print(f"\nCurrent time: {current_data['time']}")
        print(f"Current temperature_2m: {current_data['temperature_2m']}")
        print(f"Current relative_humidity_2m: {current_data['relative_humidity_2m']}")
        print(f"Current precipitation: {current_data['precipitation']}")
        print(f"Current weather_code: {current_data['weather_code']}")
        print(f"Current wind_speed_10m: {current_data['wind_speed_10m']}")
        print(f"Current wind_direction_10m: {current_data['wind_direction_10m']}")
        print(f"Current apparent_temperature: {current_data['apparent_temperature']}")
        print(f"Current is_day: {current_data['is_day']}")

        # Process hourly data. The order of variables needs to be the same as requested.
        # Getting only the hourly weather dictionary from the json
        hourly = data['hourly']
        


    else:
        # if there is any other error it will show the status code and error message
        print("Error:", responses.status_code)

except requests.exceptions.RequestException as err:
    print("Error:", err)
