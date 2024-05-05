def hours_to_seconds(hours):
    return hours * 3600  # 1 hour = 3600 seconds

# Example usage
hours = int(input("Enter the hour: "))
seconds = hours_to_seconds(hours)
print(f"{hours} hours is equal to {seconds} seconds.")
