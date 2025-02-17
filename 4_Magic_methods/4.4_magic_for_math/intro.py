class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}: {self.age}"
    
    def __add__(self, n):
        return self.age + n
        
cat = Cat("Bob", 12)

cat += 10
print(cat)