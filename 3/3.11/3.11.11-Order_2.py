class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.balance += value

    def is_money_enough(self, value):
        return self.balance >= value

    def payment(self, value):
        if not self.is_money_enough(value):
            print("Не хватает средств на балансе. Пополните счет")
            return None
        self.balance -= value

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'
