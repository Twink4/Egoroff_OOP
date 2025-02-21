class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, value):
        if isinstance(value, Rectangle):
            return self.a == value.a and self.b == value.b or\
                self.a == value.b and self.b == value.a
        return False


num = Rectangle(2, 3)

print(num == Rectangle(3, 2))
