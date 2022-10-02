#import other.py scripts
from binancedatapull import minutes_of_new_data, get_all_binance
from add_indicators import add_indicators
from model import model
from check_decimals import check_decimals
from sell_coins import sell_coins
from buy_coins import buy_coins


#import packages
from binance.client import Client
import pandas as pd
import numpy as np
from ta import add_all_ta_features
from datetime import timedelta, datetime  
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ta import add_all_ta_features
from ta.utils import dropna
import time


def buy_binance(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        #pull data
        binance_symbols = ['ADABTC', 'ALGOBTC', 'ATOMBTC', 'BANDBTC', 'BATBTC', 'BCHBTC', 'BNBBTC', 'COMPBTC', 'DAIBTC', 'DASHBTC', 'DOGEBTC',
        'EGLDBTC', 'ENJBTC', 'EOSBTC', 'HBARBTC','HNTBTC', 'ICXBTC', 'IOTABTC', 'KNCBTC', 'LINKBTC',  'MANABTC', 'MATICBTC', 'MKRBTC',
        'NANOBTC', 'NEOBTC', 'OMGBTC', 'ONEBTC', 'ONTBTC', 'OXTBTC', 'PAXGBTC', 'QTUMBTC','REPBTC', 'RVNBTC', 'SOLBTC', 'STORJBTC', 'UNIBTC',
        'VETBTC',  'WAVESBTC',  'XLMBTC', 'XTZBTC', 'ZECBTC', 'ZENBTC',  'ZILBTC','ZRXBTC']
        #binance_symbols = ['ADABTC', 'ALGOBTC', 'ATOMBTC']
        df = pd.DataFrame([])
        for symbol in binance_symbols:
            df1 = get_all_binance(symbol, '1d', save = True)
            df1['coin'] = symbol
            df = df.append(df1, True)
        cols=[i for i in df.columns if i not in ["coin"]]
        for col in cols:
            df[col]=pd.to_numeric(df[col])
        #add indicators
        df = add_indicators(df)
        array = model(df)
        #BINANCE INFO
        api_key = ''
        api_secret = ''
        binance_client = Client(api_key, api_secret,tld='us')
        #BINANCE SELL STUFF
        sell_coins()
        #BINANCE BUY STUFF
        buy_coins(array)
        return f'Hello World!'
