class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return f"Rectangle {self.a}x{self.b}"

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"Square {self.a}x{self.a}"
    
    def get_area(self):
        return self.a**2
    

class Circle:
    def __init__(self, r):
        self.r = r
        
    def __str__(self):
        return f"Circle with radius={self.r}"

    def get_area(self):
        return 3.14 * self.r**2


rect1 = Rectangle(5, 4)
rect2 = Rectangle(4, 10)

sq1 = Square(4)
sq2 = Square(10)

figures = [rect1, rect2, sq1,  sq2]

for figure in figures:
    print(figure, figure.get_area())