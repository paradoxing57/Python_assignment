class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Current balance for account {self.account_number}: ${self.balance}")


# Example usage
account1 = BankAccount("12345", "John Doe", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()

account2 = BankAccount("67890", "Jane Smith")
account2.deposit(1500)
account2.withdraw(300)
account2.check_balance()
