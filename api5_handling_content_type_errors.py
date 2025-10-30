import requests

# Add a header to use in the request
# For example server can't reply in xml format
headers = {'accept': 'application/xml'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
# 406 Not Available means it can't reply in the requested format
if response.status_code == 406:
    print('The server can not respond in XML')

    # Print the accepted content types from the response of the server
    print('These are the content types the server accepts: ' + response.headers['accept'])

# if it can reply in that format this runs
else:
    print(response.text)