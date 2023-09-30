import math
def optimal_bet_percentage(success_rate, win_amount, loss_amount):
  # Calculate the expected value of the bet.
  expected_value = success_rate * win_amount + (1 - success_rate) * loss_amount

  # Calculate the variance of the bet.
  variance = success_rate * (1 - success_rate) * (win_amount - loss_amount)**2

  # Calculate the optimal bet size using the Kelly criterion.
  optimal_bet_size = math.sqrt(expected_value / variance)

  # Return the optimal bet size as a percentage.
  return optimal_bet_size * 100
print(optimal_bet_percentage(95, 1.5, 0))