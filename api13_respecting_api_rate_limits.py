import time
import requests

# if the status code returns 429 which means Limit is hit and we have to wait
for i in range(5):
    response = requests.get("https://api.example.com/data")
    if response.status_code == 429:
        print("Rate limit hit! Waiting 60 seconds...")
        # Wait for 60 seconds before making the next request
        time.sleep(60)
    else:
        print(response.json())