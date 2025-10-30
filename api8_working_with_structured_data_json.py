import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)
data = response.json()

# Access a field like a dictionary
print(data["name"])
print(data["address"]["city"])  # Nested field