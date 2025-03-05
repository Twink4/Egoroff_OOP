class Quadrilateral:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height else width

    def __str__(self):
        return f"{'Квадрат' if self else 'Прямоугольник'} размером {self.width}х{self.height}"

    def __bool__(self):
        return self.width == self.height


q1 = Quadrilateral(10)
print(q1)
print(bool(q1))
print(isinstance(q1, Quadrilateral))
q2 = Quadrilateral(3, 5)
print(q2)
print(bool(q2))

q3 = Quadrilateral(4, 7)
print(q3)
print(bool(q3))
