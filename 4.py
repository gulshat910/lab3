class BankAccount:
    def __init__(self): # Инициализация банковского счёта с нулевым балансом и пустым списком транзакций
        self._balance = 0 # Приватный атрибут для хранения баланса счёта
        self._transactions = [] # Приватный атрибут для хранения истории транзакций

    def deposit(self, amount): # Метод для внесения депозита на счёт
        if amount > 0:
            self._balance += amount # Увеличение баланса на сумму депозита
            self._transactions.append(f"Депозит: +{amount}")  # Добавление транзакции в историю
        else:
            print("Ошибка: сумма депозита должна быть положительной.")

    def withdraw(self, amount): # Метод для снятия средств со счёта
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Снятие: -{amount}")
        else:
            print("Ошибка: сумма снятия должна быть положительной и не превышать баланс счёта.")

    @property
    def balance(self): # Геттер для получения текущего баланса счёта
        return self._balance
