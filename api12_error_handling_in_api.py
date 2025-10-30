import requests

# We can use try/except to catch network issues or server errors.
# Using Different type of errors
try:
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()   # Raises an HTTPError for bad codes
    print(response.json())
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Error:", err)
