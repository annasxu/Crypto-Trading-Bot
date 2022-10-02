from binance.client import Client
import time  
from check_decimals import check_decimals

api_key = ''
api_secret = ''
binance_client = Client(api_key, api_secret,tld='us')

def buy_coins(array):
    one_third_account_total = (int(float(binance_client.get_asset_balance(asset='USD')["free"]))-5)/3-1
    print(one_third_account_total)
    for i in array:
        print(i)
        try:
            coin = i.replace('BTC','USD')
            price = binance_client.get_symbol_ticker(symbol=coin)
            quantity = round(one_third_account_total/float(price["price"]),check_decimals(coin, binance_client))
            buy_order = binance_client.create_order(symbol=coin, side='BUY', type='MARKET', quantity=quantity)
            print('ordered' + str(i))
        except:
            coin = i.replace('BTC','USDT')
            price = binance_client.get_symbol_ticker(symbol=coin)
            quantity = round(one_third_account_total/float(price["price"]),check_decimals(coin, binance_client))
            buy_order = binance_client.create_order(symbol='USDTUSD', side='SELL', type='MARKET', quantity=quantity*1.1)
            buy_order = binance_client.create_order(symbol=coin, side='BUY', type='MARKET', quantity=quantity)
            print('ordered' + str(i))