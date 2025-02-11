import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00      # New minimum price
MAX_PRICE = 100.00    # New maximum price
INITIAL_PRICE = 10.00
FILENAME = "stock_price_simulation.txt"  # Output file name

# Initialize variables
price = INITIAL_PRICE
number_of_days = 0

# Open the output file once before the simulation loop
out_file = open(FILENAME, 'w')

# Print the starting price
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate the stock price changes
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    price_change = 0

    # Generate a random integer of 1 or 2 for increase/decrease
    if random.randint(1, 2) == 1:
        # Price increases
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Price decreases
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Update the price
    price *= (1 + price_change)

    # Output the day and the price to the file
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Closing output file
out_file.close()
