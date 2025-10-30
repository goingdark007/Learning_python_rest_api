import requests # importing requests package

"""Headers"""

# Adding headers to a request. Just use the headers= {} parameter in get and post,
# and make sure it takes key-value pair in the form of a dictionary. Using this we
# can add as many headers as we want to our request.
response = requests.get(
    'https://api.datacamp.com',
    headers= {'accept' : 'application/json'}
)

# We can access individual response headers by sub setting the dictionary
# using [] square brackets
print(response.headers['content-type'])

# Or by using .get() method on the dictionary.
response.headers.get('content-type')


"""Status Codes"""

# Accessing the status code. Each response object has a status-code
# attribute which contains the numeric value of the status-code.
# We can access the status message by using .status_code method.
print(response.status_code == 200) # True if is status code is 200

# We also have an easy look up instead of remembering the status-code.
# By using requests.codes look up object with the status message.
# We can easily find any status code without knowing it.
print(response.status_code == requests.codes.not_found) # True if no status code is found