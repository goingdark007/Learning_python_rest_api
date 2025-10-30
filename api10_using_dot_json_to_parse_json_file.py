import requests

# When we make a GET request, use .json() to parse it easily.
response = requests.get("https://api.github.com/users/octocat")
if response.status_code == 200:
    data = response.json()
    print(data["login"])
else:
    print("Error:", response.status_code)
