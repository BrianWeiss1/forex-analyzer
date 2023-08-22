def calculate_200ema(data, amount):
    ema = data['close'].ewm(span=amount, adjust=False).mean()
    return ema
def greaterThenCurrent(current_price, EMA):
    if current_price > EMA:
        return True
    elif current_price < EMA:
        return False
    return None