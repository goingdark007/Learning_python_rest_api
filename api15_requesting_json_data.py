import requests

# We can pass query parameters using params.
# In query parameter we can set headers or queries
# like userId as 1 which means return JSON.
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}

response = requests.get(url, params=params)
print(response.json())