# CP1404/CP5632 Practical - File Reading Techniques

# Function to write a name to a file
def write_name_to_file():
    with open("name.txt", "w") as out_file:
        name = input("What is your name? ")
        print(name, file=out_file)

# Function to read a name from a file
def read_name_from_file():
    with open("name.txt", "r") as in_file:
        return in_file.read().strip()

# Function to read the first two numbers from a file and return their sum
def sum_first_two_numbers(file_name):
    with open(file_name, "r") as in_file:
        number1 = int(in_file.readline())
        number2 = int(in_file.readline())
        return number1 + number2

# Function to calculate the total of all numbers in a file
def total_numbers(file_name):
    total = 0
    with open(file_name, "r") as in_file:
        for line in in_file:
            total += int(line.strip())
    return total

# Main program logic
write_name_to_file()
name = read_name_from_file()
print(f"Hi {name}!")

# The file 'numbers.txt' should exist and contain valid integers
sum_result = sum_first_two_numbers("numbers.txt")
print(f"The sum of the first two numbers is: {sum_result}")

total_result = total_numbers("numbers.txt")
print(f"The total of all numbers is: {total_result}")