# urllib bundled with python but not user-friendly
from urllib.request import urlopen

api = "http://api.music-catalog.com/"

with urlopen(api) as response:
    data = response.read()
    string = data.decode()
    print(string)

# requests easier to use and built-in features

import requests

api = "http://api.music-catalog.com/"

response = requests.get(api)

print(response.text)