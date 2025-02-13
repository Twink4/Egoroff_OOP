class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return "Name: {}\nPrice: {}\nQuantity: {}"\
            .format(self.name, self.price, self.quantity)

    def __repr__(self):
        return f"GroceryItem({self.name}, {self.price}, {self.quantity})"
