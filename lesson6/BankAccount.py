# Create a Python class called "BankAccount" with the following fields and methods:

# Fields:
# account_number (string)
# balance (float)
# Methods:
# deposit(amount): Adds the specified amount to the account balance.
# withdraw(amount): Subtracts the specified amount from the account balance. Ensure that the account has sufficient funds before allowing the withdrawal.
# get_balance(): Returns the current account balance.

class BankAccount:

    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
account = BankAccount('User1', 100)
print(account.get_balance())
account.deposit(1000)
account.withdraw(500)
print(account.get_balance())