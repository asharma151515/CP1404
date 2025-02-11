# randoms.py

import random

# Explore the random module using dir()
print("Exploring the random module:")
print(dir(random))

# Getting information about the randint and randrange functions using help()
print("\nHelp on random.randint:")
help(random.randint)

print("\nHelp on random.randrange:")
help(random.randrange)

# Generating random numbers
# Random integer between 5 and 20 (inclusive) using random.randint()
random_number1 = random.randint(5, 20)  # line 1
print(f"\nRandom number from randint(5, 20): {random_number1}")

# Random number between 3 and 10 (exclusive) stepping by 2 using random.randrange()
random_number2 = random.randrange(3, 10, 2)  # line 2
print(f"Random number from randrange(3, 10, 2): {random_number2}")

# Random float between 2.5 and 5.5 using random.uniform()
random_number3 = random.uniform(2.5, 5.5)  # line 3
print(f"Random number from uniform(2.5, 5.5): {random_number3}")

# Generating a random number between 1 and 100 (inclusive)
random_number4 = random.randint(1, 100)  # New random number generation
print(f"\nRandom number between 1 and 100 inclusive: {random_number4}")

# Conclusion of the random number generation demonstration
print("\nRandom number generation completed.")