import requests
import json

def get_btc_data(start_date, end_date):
  url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=30m&startTime={}&endTime={}".format(start_date, end_date)
  response = requests.get(url)
  data = json.loads(response.content)
  return data

def main():
  start_date = "49315200"
  end_date = "05-09"
  data = get_btc_data(start_date, end_date)
  print((data))

if __name__ == "__main__":
  main()