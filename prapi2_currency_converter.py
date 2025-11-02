import requests

url = "https://api.fastforex.io/fetch-one"


query_params = {

    'api_key' : 'b92b0ae420-a151890833-t53fpj',
    'from'  : 'USD',
    'to' : 'BDT'

}

response = requests.get(url, params= query_params)

data = response.json()

convertion_rate = data['result']['BDT']

usd_amount = 123

print(f'123 dollars is {usd_amount * convertion_rate} Taka')

bdt_amount = 4500

print(f'4500 taka is {bdt_amount / convertion_rate} dollars')

