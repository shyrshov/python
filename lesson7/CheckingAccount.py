# CheckingAccount:

# Additional attribute: transaction_fee (float): The fee charged for each transaction (withdrawal, deposit).
# Additional method: deduct_transaction_fee(): Deducts the transaction fee from the account balance after each transaction.
# Implement encapsulation to ensure that the account balance is not accessed directly from outside the class.

from Account import Account

class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, transaction_fee: float):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        self._balance -= self.transaction_fee

    