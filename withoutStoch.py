
def calculate_stochastic_oscillator(closing_prices, k_period, d_period, smoothing_period, api_key):
    if len(closing_prices) < k_period:
        return None, None

    k_values = []
    for i in range(len(closing_prices) - k_period + 1):
        highest_high = max(closing_prices[i : i + k_period])
        lowest_low = min(closing_prices[i : i + k_period])
        k_value = ((closing_prices[i + k_period - 1] - lowest_low) / (highest_high - lowest_low)) * 100
        k_values.append(k_value)

    d_values = [sum(k_values[i : i + d_period]) / d_period for i in range(len(k_values) - d_period + 1)]

    if len(d_values) < smoothing_period:
        return None, None

    smoothed_d_values = [sum(d_values[i : i + smoothing_period]) / smoothing_period for i in range(len(d_values) - smoothing_period + 1)]

    return k_values[-1], smoothed_d_values[-1]

# Replace with your Alpha Vantage API key
api_key = "YOUR_API_KEY"

# Replace with your dataset of closing prices, %K period, %D period, and smoothing period
closing_prices = [120.5, 122.3, 124.7, 121.8, 119.6, 125.2, 124.1, 126.0, 123.5, 120.9]
k_period = 5
d_period = 3
smoothing_period = 3

percentK, percentD = calculate_stochastic_oscillator(closing_prices, k_period, d_period, smoothing_period, api_key)
print("Last %K:", percentK)
print("Last %D:", percentD)