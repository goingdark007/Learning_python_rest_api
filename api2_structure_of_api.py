# Customize the URL to interact with specific API resources.
# # http:// is the protocol which is the means of transportation.
# # 350.5th-ave.com is the domain which is the street address the office building.
# # :80 is the port which is the gate or door to use when entering the building.
# # /unit/243 is the path which is the specific office unit inside the building.
# # ?floor=77 is the query which is any additional instructions.
# http://	350.5th-ave.com	:80	/unit/243	?floor=77

""" Adding query with requests. """
# Append the query to the URL string directly
import requests

response = requests.get("http://350.5th-ave.com:80/unit/243?floor=77&elevator=True")

print(response.url)

# We can use the params argument to add query parameters. Create a dictionary.
query_params = {
    'floor': 77,
    'elevator' : True
}

# pass the dictionary using the params argument.
response2 = requests.get("http://350.5th-ave.com:80/unit/243", params=query_params)
print(response2.url)