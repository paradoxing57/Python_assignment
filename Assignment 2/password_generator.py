import random
import string

def generate_password(length=12):
    # Define character sets for password generation
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation  # You can customize this with special characters you want

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate a strong password using random.choices
    password = ''.join(random.choices(all_characters, k=length))
    return password

# Example usage
password_length = 16  # You can specify the desired password length here
strong_password = generate_password(password_length)
print("Strong Password:", strong_password)
