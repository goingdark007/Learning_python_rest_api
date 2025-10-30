import time
import requests

# APIs often limit requests per minute/hour. If we exceed it,
# we might get 429 Too Many Requests. Use a loop and time.sleep(60)
# to fix it.
for i in range(5):
    response = requests.get("https://api.example.com/data")
    if response.status_code == 429:
        print("Rate limit hit! Waiting 60 seconds...")
        time.sleep(60)
    else:
        print(response.json())

# use headers like X-RateLimit-Remaining if the API provides them:
# print(response.headers.get("X-RateLimit-Remaining"))
