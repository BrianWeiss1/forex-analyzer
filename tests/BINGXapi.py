import requests
import hmac
from hashlib import sha256

API_URL = "https://open-api.bingx.com"
API_KEY = "YOUR_API_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"

def get_signature(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    return signature

def build_request_object(symbol, contract_type, side, quantity, price, order_type):
    request_object = {
        "symbol": symbol,
        "contract_type": contract_type,
        "side": side,
        "quantity": quantity,
        "price": price,
        "order_type": order_type
    }
    return request_object

def send_request(request_object):
    url = f"{API_URL}/api/v1/swap/order/place"
    headers = {
        "X-BX-APIKEY": API_KEY,
        "X-BX-SIGNATURE": get_signature(SECRET_KEY, request_object)
    }
    response = requests.post(url, headers=headers, json=request_object)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to send request: {response.status_code} {response.content}")

# Example request to place a perpetual derivatives order
request_object = build_request_object(symbol="BTCUSDT", contract_type="PERPETUAL", side="BUY", quantity=1, price=10000, order_type="LIMIT")

# Send the request and get the response
response = send_request(request_object)

# Print the response
print(response)
