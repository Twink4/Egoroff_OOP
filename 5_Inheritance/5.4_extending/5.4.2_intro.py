class Person:
    
    age = 25
    
    def breathe(self):
        print('Человек дышит')
        
    def sleep(self):
        print('Человек спит')
        
    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()
        if hasattr(self, 'age'):
            print(self.age)
    
    
class Doctor(Person):
    
    age = 33
    
    def breathe(self):
        print('Доктор дышит')
    
    def sleep(self):
        print('Доктор спит')
        
    def walk(self):
        print('Доктор идет')
        

p = Person()
p.combo()

d = Doctor()
d.combo()