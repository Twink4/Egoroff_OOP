class Order:
    def __init__(self, cart: list, customer):
        self.cart: list = cart
        self.customer = customer

    def __add__(self, product):
        return Order(self.cart + [product], self.customer)

    def __radd__(self, product):
        return Order([product] + self.cart, self.customer)

    def __sub__(self, product):
        if product in self.cart:
            self.cart.remove(product)
        return Order(self.cart, self.customer)

    def __rsub__(self, product):
        return self.__sub__(product)


order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')
