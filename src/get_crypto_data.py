import requests
import pandas

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

result = requests.get(url=url)

data = result.json()

print(data['bpi']["USD"]["rate_float"])
