# Take user input
num_str = input("Enter a number: ")

# Check if the input is a valid integer
try:
    num = int(num_str)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
