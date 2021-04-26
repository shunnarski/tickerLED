import requests
import pandas
from coinbase.wallet.client import Client
import os
from api_keys import COINBASE_API_KEY, COINBASE_API_SECRET

def get_crypto_price(crypto_ticker):

    client = Client(api_key=COINBASE_API_KEY, api_secret=COINBASE_API_SECRET)
    currency_code = "USD"
    price = client.get_spot_price(currency=currency_code)
    return price
