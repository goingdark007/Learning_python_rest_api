import requests

# GET keyword is used to retrieve a response
response = requests.get('link')

# POST is used to create a response
# For post and put requests we need to add data to create or update our resources
# By passing a data argument to specify the data to be sent
response2 = requests.post('link', data = {'key': 'value'})

# PUT is used to update an existing resource
response3 = requests.put('link', data = {'key': 'value'})

# DELETE is used to remove a resource just like get function
response4 = requests.delete('link')
