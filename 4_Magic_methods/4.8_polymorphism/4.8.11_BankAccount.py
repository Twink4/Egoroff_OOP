class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __lt__(self, value):
        return self.balance < value

    def __gt__(self, value):
        return self.balance > value


values = [BankAccount('Petrovich', 400), 500, BankAccount('Andrey', 200), 100, BankAccount('Zina', 150)]
values.sort()
print(*values)
