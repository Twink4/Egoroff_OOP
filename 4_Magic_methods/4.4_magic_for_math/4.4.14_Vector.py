class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if type(i) is int])
    
    def __check_len(self, value):
        return len(self.values) == len(value.values)
    def __str__(self):
        return f"Вектор{tuple(self.values)}" if self.values else "Пустой вектор"
    
    def __add__(self, value):
        if type(value) is int:
            return Vector(*(i + value for i in self.values))
        if type(value) is Vector:
            if self.__check_len(value):
                return Vector(*(self.values[k] + v for k, v in enumerate(value.values)))
            else:
                print("Сложение векторов разной длины недопустимо")
        print(f"Вектор нельзя сложить со значением {value}")
        
    def __mul__(self, value):
        ...
        
v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"