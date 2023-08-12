import requests
import pandas as pd

def get_forex_prices(currency_pair, start_date, end_date):
    """Gets the prices of a forex commodity in 1 minute intervals.

    Args:
        currency_pair (str): The forex currency pair, e.g. "USDEUR".
        start_date (str): The start date of the data in YYYY-MM-DD format.
        end_date (str): The end date of the data in YYYY-MM-DD format.

    Returns:
        pd.DataFrame: A Pandas DataFrame with the prices and time in 1 minute intervals.
    """

    url = "https://api.exchangeratesapi.io/history?start_date={start_date}&end_date={end_date}&base={currency_pair}&access_key=f5b2765c8ba1118f69fd39005775ff38".format(
        start_date=start_date,
        end_date=end_date,
        currency_pair=currency_pair,
    )
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        print(data)
        prices = data["rates"]["USD"]
        times = data["timestamps"]
        df = pd.DataFrame({"price": prices, "time": times})
        df["time"] = pd.to_datetime(df["time"])
        df = df.set_index("time")
        return df
    else:
        raise Exception("Error getting forex prices: {}".format(response.status_code))

def stochastic(df, k_value, d_value, smoothing_value):
    """Calculates the %K and %D values of the Stochastic Oscillator.

    Args:
        df (pd.DataFrame): The Pandas DataFrame with the prices and time in 1 minute intervals.
        k_value (int): The K-value of the Stochastic Oscillator.
        d_value (int): The D-value of the Stochastic Oscillator.
        smoothing_value (int): The smoothing value of the Stochastic Oscillator.

    Returns:
        list: A list of the %K and %D values.
    """

    min_price = df["price"].rolling(k_value).min()
    max_price = df["price"].rolling(k_value).max()
    percentk = 100 * (df["price"] - min_price) / (max_price - min_price)
    percentk = percentk.ewm(span=smoothing_value).mean()
    percentd = percentk.ewm(span=d_value).mean()
    return [percentk, percentd]

if __name__ == "__main__":
    currency_pair = "USDEUR"
    start_date = "2023-08-01"
    end_date = "2023-08-10"
    k_value = 14
    d_value = 3
    smoothing_value = 3

    df = get_forex_prices(currency_pair, start_date, end_date)
    percentk, percentd = stochastic(df, k_value, d_value, smoothing_value)

    print("The %K value is:", percentk[-1])
    print("The %D value is:", percentd[-1])
