from binance.client import Client

api_key = 'lYvlv5kPTPaXotnXhEN17tyV4JP7EEyBHl5bMnVMo7Nrvi6rahX56TrkPcFyKTrq'
api_secret = 'GCFMK0fV4EZ4LC5ZoGofa93AiZDMkWCJsUwIMgDjEse9FiAwcUKlnxRSkoun7JrU'
binance_client = Client(api_key, api_secret,tld='us')

def check_decimals(symbol, binance_client):
    info = binance_client.get_symbol_info(symbol)
    val = info['filters'][2]['stepSize']
    decimal = 0
    is_dec = False
    for c in val:
        if is_dec is True:
            decimal += 1
        if c == '1':
            break
        if c == '.':
            is_dec = True
    return decimal
