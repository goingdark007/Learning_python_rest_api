import requests

# Key as query parameter
url = "https://api.weatherapi.com/v1/current.json"
params = {
    "key": "our_api_key",
    "q": "London"
}

response = requests.get(url, params=params)
print(response.json())

# Key in headers
headers = {
    "Authorization": "Bearer our_api_key"
}
response = requests.get("https://api.example.com/data", headers=headers)
print(response.json())
