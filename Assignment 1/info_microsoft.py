class Programmer:
    def __init__(self, name, employee_id, position):
        self.name = name
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")

# Example usage
programmer1 = Programmer("John Doe", "MS1234", "Software Engineer")
programmer2 = Programmer("Jane Smith", "MS5678", "Data Scientist")

# Display information about the programmers
print("Programmer 1:")
programmer1.display_info()
print("\nProgrammer 2:")
programmer2.display_info()
