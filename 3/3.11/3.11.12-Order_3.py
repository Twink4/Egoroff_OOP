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
            return False
        self.balance -= value
        return True

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self, User: User):
        self.user = User
        self.goods = {}
        self.__total = 0

    def add(self, Product: Product, count=1):
        if Product.name not in self.goods.keys():
            self.goods[Product] = count
        else:
            self.goods[Product] += count
        self.__total += Product.price * count

    def remove(self, Product: Product, count=1):
        if self.goods[Product] >= count:
            self.goods[Product] -= count
        else:
            count = self.goods[Product]
            del self.goods[Product]
        self.__total -= Product.price * count

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")

    def print_check(self):
        goods = sorted(self.goods.items(), key=lambda x: x[0].name)
        print("---Your check---")
        for product, count in goods:
            name = product.name
            price = product.price
            print(f'{name} {price} {count} {price * count}')
        print(f"---Total: {self.total}---")


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total)  # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order()  # Заказ оплачен
print(cart_billy.user.balance)  # 20
