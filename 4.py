class BankAccount:
    def __init__(self):
        self._balance = 0
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append("Deposit: +{amount}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._transactions.append("Withdraw: -{amount}")
        else:
            print("Invalid amount for withdrawal.")
