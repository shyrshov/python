# Write a simple program that creates instances of both SavingsAccount and CheckingAccount. 
# Perform some deposits, withdrawals, and interest calculations on these accounts. Display the account summary after each transaction.

from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

savings = SavingsAccount(1, 1000, 10)

savings.deposit(2000)
print(savings._balance)
savings.withdraw(300)
print(savings._balance)
print(savings.calculate_interest())
savings.account_summary(savings)

checking = CheckingAccount(2, 2000, 20)
checking.deposit(2000)
print(checking._balance)
checking.withdraw(300)
print(checking._balance)
checking.deduct_transaction_fee()
savings.account_summary(checking)
