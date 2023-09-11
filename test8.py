# Define the initial portfolio value and parameters
initial_portfolio = 10
bet_percentage = 0.001
growth_rate = 1.75
return_rate = 1.75  # 10% return

# Create lists to store the portfolio values and x values
portfolio_values = [initial_portfolio]
x_values = [0]

# Define the number of iterations
num_iterations = 50  # You can change this value to determine how many iterations to graph

# Calculate the portfolio values for each iteration
for x in range(1, num_iterations + 1):
    portfolio = portfolio_values[-1] * growth_rate - bet_percentage * portfolio_values[-1]
    portfolio = return_rate * portfolio  # Apply the return
    portfolio_values.append(portfolio)
    x_values.append(x)
print(x_values[0])
print(portfolio_values[-1])
# Plot the portfolio values over time
plt.plot(x_values, portfolio_values)
plt.xlabel('Iteration (x)')
plt.ylabel('Portfolio Value')
plt.title('Portfolio Growth Over Time')
plt.grid(True)
plt.show()
