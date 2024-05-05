# Accept input from the user
input_str = input("Enter a sequence of comma-separated numbers: ")

# Split the input string into a list of numbers
num_list = [int(num) for num in input_str.split(',')]

# Convert the list to a tuple
num_tuple = tuple(num_list)

# Print the list and tuple
print("List:", num_list)
print("Tuple:", num_tuple)
