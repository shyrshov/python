# Create a base class called Account, which will have the following attributes and methods:
# Attributes:

# account_number (int): A unique identifier for each account.
# balance (float): The current balance of the account.
# Methods:

# deposit(amount: float): Adds the given amount to the account balance.
# withdraw(amount: float): Subtracts the given amount from the account balance if sufficient funds are available.

from abc import ABC

class Account(ABC):
    def __init__(self, account_number: int, balance: float):
        self.account_number = account_number
        self._balance = balance
    
    def deposit(self, amount: float):
        self._balance += amount

    def withdraw(self, amount: float):
        self._balance -= amount
