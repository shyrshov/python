# SavingsAccount:

# Additional attribute: interest_rate (float): The annual interest rate on the savings account.
# Additional method: calculate_interest(): Calculates and returns the interest earned for a month based on the current balance and interest rate.

# Demonstrate polymorphism by creating a function called account_summary(account: Account) that takes an Account object as an argument 
# and prints a summary of the account, including the account type, account number, and current balance.


from Account import Account
from CheckingAccount import CheckingAccount


class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: float, interest_rate: float):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self._balance * self.interest_rate / 12
    
    def account_summary(self, account):
        if isinstance(account, SavingsAccount):
            print("Account type: Saving Account")
        elif isinstance(account, CheckingAccount):
            print("Account type: Checking Account")
        print("Account Number: ", account.account_number)
        print("Current Balance: ", account._balance)