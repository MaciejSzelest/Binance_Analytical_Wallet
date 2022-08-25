from binance.client import Client
import pandas as pd
import os
import requests
import json

# PANDAS: OPTIONS ######################################################################################################

pd.set_option('float_format', '{:f}'.format)
pd.options.mode.chained_assignment = None

# CLASS: BINANCE #######################################################################################################


class Binance(object):

    def __init__(self):
        None

    def __str__(self):
        ret = 'Class Binance'
        return ret

    def login(self):
        api_key = os.environ['api_key']
        api_secret = os.environ['api_secret']
        client = Client(api_key, api_secret)
        return client
        client.close_connection()

    def history(symbol):
        client = Binance.login(object)
        trades = client.get_my_trades(symbol=symbol)
        trades_df = pd.DataFrame(trades)
        df = trades_df[['symbol', 'id', 'isBuyer', 'time', 'price', 'qty', 'quoteQty']]
        df['qty'] = df['qty'].astype(float)
        df['quoteQty'] = df['quoteQty'].astype(float)
        df['price'] = df['price'].astype(float)
        df['Factor'] = df['isBuyer'].apply(lambda x: -1 if x == False else 1)
        df['qty'] = df['qty'] * df['Factor']
        df['quoteQty'] = df['quoteQty'] * df['Factor']
        return df
        client.close_connection()

    def price(symbol):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=" + symbol
        price = requests.get(key)
        price = price.json()
        df = pd.json_normalize(price)
        df['price'] = df['price'].astype(float)
        return df

    def account(symbol):
        account = Binance.history(symbol)
        price = Binance.price(symbol)
        df = account.merge(price, how='left', on='symbol')
        df['Profit/Loss Price'] = df['price_y'] / df['price_x']
        df['Holdings'] = df['quoteQty'] * df['Profit/Loss Price']
        df['Profit/Loss'] = df['Holdings'] - df['quoteQty']
        df['Volume'] = df['Holdings'].cumsum()
        df['time'] = pd.to_datetime(df['time'], unit="ms")
        return df

    def hist_price(symbol):
        root_url = 'https://api.binance.com/api/v1/klines'
        url = root_url + '?symbol=' + symbol + 'USDT' + '&interval=1d'
        dataset = json.loads(requests.get(url).text)
        df = pd.DataFrame(dataset)
        df.columns = ['ot', 'o', 'h', 'l', 'Price', 'v', 'Date', 'qav', 'nt', 'tbv', 'tqv', 'ignore']
        df['Price'] = df['Price'].astype(float)
        df['Date'] = pd.to_datetime(df['Date'], unit="ms")
        df['Asset'] = symbol
        return df[['Date', 'Price', 'Asset']].round({'Price': 2})

Binance.hist_price('ADA')

if __name__ == "__main__":
    print('This is a Binance class to get connection with account via API')
    input('\n\n Press a key to close')
