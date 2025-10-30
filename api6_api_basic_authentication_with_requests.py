import os

import requests
from requests.auth import HTTPBasicAuth

# auth= HTTPBasicAuth() this method uses our username and password (like a login).
# HTTPBasicAuth sends credentials in the request header (encoded in base64).
# If correct, the server returns our authorized data (like user profile info).
url = "https://api.example.com/user"
response = requests.get(url, auth=HTTPBasicAuth("username", "password"))

print(response.status_code)
print(response.json())

# Never hardcode real passwords in our script; use environment variables instead if possible
username = os.getenv("API_USER")
password = os.getenv("API_PASS")

response = requests.get("https://api.example.com/user", auth=HTTPBasicAuth(username, password))