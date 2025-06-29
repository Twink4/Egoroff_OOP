class Person:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def __str__(self):
        return f"Person {self.name} {self.surname}"
    
    def info(self):
        print("Parent class")
        print(self)
    
    def breathe(self):
        print('Человек дышит')
        

class Doctor(Person):
    
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age
        
    def __str__(self):
        return f"Doctor {self.name} {self.surname}"
    
    def breathe(self):
        print('Доктор дышит')
        super().breathe()
        

p = Person('Ivan', 'Ivanov')
d = Doctor('Lol', 'Loloev', 36)
print(p.name, p.surname)
print(d.name, d.surname, d.age)
d.info()