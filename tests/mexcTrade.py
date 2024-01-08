import requests
import time
import hashlib
import hmac
import sys
import importlib.util

file_path = '/etc/decoder.py'
from enum import Enum

class Side(Enum):
    BUY = 1
    SELL = 2

class OrderType(Enum):
    LIMIT = "Limit order"
    MARKET = "Market order"
    LIMIT_MAKER = "Limit maker order"
    IMMEDIATE_OR_CANCEL = "Immediate or cancel order"
    FILL_OR_KILL = "Fill or kill order"

# Load the module
spec = importlib.util.spec_from_file_location("decode", file_path)
decode = importlib.util.module_from_spec(spec)
sys.modules["decode"] = decode
spec.loader.exec_module(decode)

# Now you can import the module as usual

def generate_signature(secret_key, query_string):
    return hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()

def openLong(symbol, betAmount, maxLev):
    # Set the necessary parameters
    with open('documents/mexc_api.txt') as f:
        api_key = f.read()
    with open('/etc/pam.d/mexcApiKey.txt.txt') as f:
        secret_key = decode.decode(f.read())
    print(type(secret_key))
    base_url = 'https://www.mexc.com'
    endpoint = '/api/v3/order'

    # Prepare the query parameters
    params = {
        'symbol': symbol,
        'side': Side.BUY,  # For a long position
        'type': OrderType.MARKET,  # A market order
        'quoteOrderQty': betAmount,  # Assuming betAmount is the amount in quote asset
        'timestamp': int(time.time() * 1000)
    }

    # Generate the signature
    query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
    signature = generate_signature(secret_key, query_string)
    params['signature'] = signature

    # Make the POST request
    headers = {'X-MBX-APIKEY': api_key}
    response = requests.post(base_url + endpoint, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: ", response.status_code, response.text)
        return response.text  # or handle the error appropriately
    return response.json()

response = openLong('BTCUSDT', 100, 10)
print(response)








