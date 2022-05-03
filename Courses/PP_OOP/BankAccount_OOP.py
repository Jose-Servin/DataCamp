class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def __eq__(self, other):
        print("__eq__() is called ")

        return self.balance == other.balance

    def __repr__(self):
        account_string = f"BankAccount(20000)"
        return account_string


# Inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        # call the Parent constructor
        BankAccount.__init__(self, balance)
        self.interest_rate = interest_rate

    def compute_interest(self, n_periods=1):
        return self.balance * ((1 + self.interest_rate) ** n_periods - 1)


class CheckingAccount(BankAccount):
    def __init__(self, balance, limit):
        BankAccount.__init__(self, balance)
        self.limit = limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, fee=0):
        if fee <= self.limit:
            # here we use the Parent class function since this functionality already exists
            BankAccount.withdraw(self, amount - fee)
        else:
            BankAccount.withdraw(self, amount - self.limit)
