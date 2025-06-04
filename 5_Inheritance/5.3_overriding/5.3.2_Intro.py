class Person:
    
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print("Человек дышит")
        
    
    def walk(self):
        print("Человек идет")
        
    def sleep(self):
        print("Человек спит")
        
    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()
        
    def __str__(self):
        return f"Person {self.name}"
        
        
class Doctor(Person):
    
    def breathe(self):
        print("Доктор дышит")
        
    def sleep(self):
        print("Доктор спит")
        
    def __str__(self):
        return f"Doctor {self.name}"
           
    
d = Doctor('John')
p = Person('Adam')

print(p, d)
p.combo()
d.combo()