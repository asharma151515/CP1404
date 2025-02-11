"""
CP1404/CP5632 - Practical
Answer the following questions:"""

# Questions
# 1. When will a ValueError occur?
# A ValueError will occur when the user inputs a non-integer value for the numerator or denominator,
# such as a string or a float that cannot be converted into an integer.

# 2. When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur when the user attempts to divide by zero, which would happen if the
# denominator is entered as zero.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, I can add a check to ensure the denominator is not zero before performing the division.



# Implementing the change:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero!")  # Manually raise ZeroDivisionError if needed
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError as e:
    print(e)  # Print the custom error message for division by zero
print("Finished.")