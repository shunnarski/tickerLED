import requests
import pandas
import interpolate_data
import os
from api_keys import YAHOO_API_KEY, YAHOO_API_HOST

def get_stock_price(stock_ticker, led_grid_width, led_grid_height):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"

    params = {
        "symbol": stock_ticker,
        "interval":"15m",
        "range":"1d",
        "region":"US"
    }

    headers = {
        'x-rapidapi-key': YAHOO_API_KEY,
        'x-raidapi-host': YAHOO_API_HOST
    }

    response = requests.request("GET", url, headers=headers, params=params)
    data = response.json()
    open_times = data['chart']['result'][0]['timestamp']
    open_prices = data['chart']['result'][0]['indicators']['quote'][0]['open']

    result_df = interpolate_data.get_interpolated_stock_prices(open_times, open_prices, led_grid_width, led_grid_height)
    
    result_df['ticker'] = stock_ticker
    
    return result_df