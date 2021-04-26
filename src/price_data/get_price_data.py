import requests
import pandas
import get_crypto_data as cd
import get_stock_data as sd
import time

LED_GRID_WIDTH = 64
LED_GRID_HEIGHT = 64

def get_crypto_price(crypto_ticker):
    price = cd.get_crypto_price(crypto_ticker)
    print("BTC Price: {}".format(price))

def get_stock_price(stock_ticker):
    prices_df = sd.get_stock_price(stock_ticker, LED_GRID_WIDTH, LED_GRID_HEIGHT)
    print(prices_df)
# get_crypto_price("BTC")

stock_tickers = ["AMZN", "TSLA", "AAPL", "MSFT"]
stock_tickers = ["AMZN"]
for stock_ticker in stock_tickers:
    get_stock_price(stock_ticker,)
    print()
    time.sleep(2)