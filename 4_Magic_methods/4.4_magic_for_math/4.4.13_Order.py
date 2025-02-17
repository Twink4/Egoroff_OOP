class Order:
    def __init__(self, cart: list, customer):
        self.cart: list = cart
        self.customer = customer
        
    def __add__(self, product):
        return Order(self.cart + [product], self.customer)
    
    def __radd__(self):
        ...
        

order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']