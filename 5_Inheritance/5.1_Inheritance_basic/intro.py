
class Person: #Родительский класс (parent)
    
    def cal_walk(self):
        print("Я могу ходить")
        
    
    def can_breathe(self):
        print("Я могу дышать")


class Doctor(Person): #Подкласс (Subclass)
    
    def can_cure(self):
        print("Я могу лечить")
        
class Ortoped(Doctor):
    ...

    
class Architect(Person): #Подкласс (Subclass)
    
    def can_build(self):
        print("Я могу построить здание")
        
        
d = Doctor()
d.can_cure()
d.cal_walk()
d.can_breathe()

a = Architect()
a.can_build()
d.cal_walk()
d.can_breathe()

e = Ortoped()
e.can_breathe()
e.cal_walk()
e.can_cure()