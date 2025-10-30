import requests

# Most APIs return JSON (JavaScript Object Notation).
# We can access the data just like a dictionary using
# the key-value pair.

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)
data = response.json()

print(data["name"])        # Access a field
print(data["address"]["city"])  # Nested field