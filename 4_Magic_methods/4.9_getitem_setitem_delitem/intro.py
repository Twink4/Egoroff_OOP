class Vector:
    def __init__(self, *args):
        self.values = list(args)
    
    def __repr__(self):
        return str(self.values)
    
    def __getitem__(self, item):
        if 1 <= item <= len(self.values): 
            return self.values[item-1]
        raise IndexError("Error. Index not found")
    
    def __setitem__(self, key, value):
        if 1 <= key <= len(self.values):
            self.values[key-1] = value
        else:
            self.values.extend([0] * (key - len(self.values)))
            self.values[key-1] = value
    
    def __delitem__(self, key):
        if 1 <= key <= len(self.values):
            del self.values[key-1]
        else:
            raise IndexError("Error. Index not found")
    
    
v1 = Vector(1, 2)
v1[1] = 15
v1[-5] = 5
print(v1)
