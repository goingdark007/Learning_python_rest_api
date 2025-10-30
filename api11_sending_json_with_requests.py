import requests

# When we need to create or update data, we send JSON.
# Using json=data automatically sets the header to
# Content-Type: application/json
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "New Post",
    "body": "Learning API with Python!",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
