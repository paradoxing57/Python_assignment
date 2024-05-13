import re

# Define the pattern you want to search for
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Example pattern for email addresses

# Read the text file
file_path = 'your_text_file.txt'  # Replace 'your_text_file.txt' with the actual file path
with open(file_path, 'r') as file:
    text = file.read()

# Search for the pattern and extract matches
matches = re.findall(pattern, text)

# Display the extracted matches
print(matches)
