import requests

# We can use try/except to catch network issues or server errors. There are multiple errors like:
# •	HTTPError – The server responded but returned an error (e.g., 404, 500).
# •	ConnectionError – There was a problem connecting to the server (no network or server down).
# •	Timeout – The request took too long to get a response from the server.
# •	RequestException – A general error that covers all other kinds of issues during a request.
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