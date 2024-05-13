import pandas as pd

# Read data from CSV file
file_path = 'your_file_path.csv'  # Replace 'your_file_path.csv' with the actual file path
data = pd.read_csv(file_path)

# Display the initial data
print("Initial data:")
print(data)

# Remove duplicates
data = data.drop_duplicates()

# Handle missing values (replace NaNs with a specified value, like 0)
data = data.fillna(0)

# Display the cleaned data
print("\nCleaned data:")
print(data)
