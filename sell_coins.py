from binance.client import Client
import time  
from check_decimals import check_decimals

api_key = ''
api_secret = ''
binance_client = Client(api_key, api_secret,tld='us')

def sell_coins():
  for i in range(0,len(binance_client.get_account()["balances"])):
      if str(binance_client.get_account()["balances"][i]['asset']) != 'USDT':
          if str(binance_client.get_account()["balances"][i]['asset']) != 'USD':  
            #currentl I am reading my USD, buying coins, selling into USDT
            try:
              coin = binance_client.get_account()["balances"][i]['asset'] + 'USD'
              usd_price = float(binance_client.get_symbol_ticker(symbol=coin)['price'])
              quantity =  float((binance_client.get_account()["balances"][i]['free']))
              time.sleep(3)
              if usd_price*quantity > 15:
                  print(binance_client.get_account()["balances"][i]['asset'])
                  coin = binance_client.get_account()["balances"][i]['asset'] + 'USD'
                  quantity = round(quantity*0.95,check_decimals(coin, binance_client))
                  sell_order = binance_client.create_order(symbol=coin, side='SELL', type='MARKET', quantity=(quantity))
            except:
              coin = binance_client.get_account()["balances"][i]['asset'] + 'USDT'
              usd_price = float(binance_client.get_symbol_ticker(symbol=coin)['price'])
              quantity =  float((binance_client.get_account()["balances"][i]['free']))
              time.sleep(3)
              if usd_price*quantity > 15:
                  print(binance_client.get_account()["balances"][i]['asset'])
                  coin = binance_client.get_account()["balances"][i]['asset'] + 'USDT'
                  quantity = round(quantity*0.95,check_decimals(coin, binance_client))
                  sell_order = binance_client.create_order(symbol=coin, side='SELL', type='MARKET', quantity=(quantity))