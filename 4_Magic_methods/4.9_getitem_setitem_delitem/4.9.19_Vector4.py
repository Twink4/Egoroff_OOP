class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __delitem__(self, value):
        if value in self.values:
            while value in self.values:
                del self.values[self.values.index(value)]
            return self.values
        else:
            raise ValueError(f"Значение {value} отсутствует в векторе")
    

v1 = Vector(5, 5, 5, 4, 4, 3)
print(v1)
del v1[4]
print(v1)
del v1[5]
print(v1)
try:
    del v1[10]
except ValueError as e:
    print(e)
    
v1 = Vector(5, 6, 7, 8, 9, 5)
del v1[6]
del v1[9]
print(v1)
del v1[5]
print(v1)