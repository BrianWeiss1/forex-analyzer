import ccxt
import importlib.util
import sys
from mexc_sdk import Spot

file_path = '/etc/decoder.py'
spec = importlib.util.spec_from_file_location("decode", file_path)
decode = importlib.util.module_from_spec(spec)
sys.modules["decode"] = decode
spec.loader.exec_module(decode)

with open('documents/mexc_api.txt') as f:
    api_key = f.read()
with open('/etc/pam.d/api_key.txt') as f:
    secret_key = decode.decode(f.read())

symbol = 'BTC/USDT:USDT'
BTCPRICE = 42705.80
USDTOBTC = 1/BTCPRICE
print(USDTOBTC*1100.5)
exchange = ccxt.mexc3({
    'apiKey': api_key,
    'secret': secret_key,
    'options': {
        'createMarketBuyOrderRequiresPrice': False
    },
})


def execute_trade(symbol, size):
    ticker = exchange.fetch_ticker(symbol)
    current_price = ticker['last']
    cost = current_price*size
    order = exchange.create_market_buy_order(symbol, size, {'price': cost})
    print('Buy Order Placed ' + str(order))
execute_trade(symbol, USDTOBTC * 1100.5)
