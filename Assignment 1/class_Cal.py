class Calculator:
    def square(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3

# Create an instance of the Calculator class
calc = Calculator()

# Take user input for a number
try:
    number = float(input("Enter a number: "))  # Convert input to float
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Calculate and display the square and cube of the number
square_result = calc.square(number)
cube_result = calc.cube(number)

print(f"Square of {number} is {square_result}")
print(f"Cube of {number} is {cube_result}")
