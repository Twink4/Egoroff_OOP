class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def get_value(value):
        return value.price if isinstance(value, Fruit) else value

    def __eq__(self, other):
        return self.price == self.get_value(other)

    def __ne__(self, other):
        return self.price != self.get_value(other)

    def __lt__(self, other):
        return self.price < self.get_value(other)

    def __le__(self, other):
        return self.price <= self.get_value(other)

    def __gt__(self, other):
        return self.price > self.get_value(other)

    def __ge__(self, other):
        return self.price >= self.get_value(other)
# Ниже код для проверки методов класса Fruit


apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')
