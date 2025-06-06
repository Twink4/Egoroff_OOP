class Doctor:
    
    def __init__(self, degree):
        self.degree = degree
    
    def graduate(self):
        print('Ура, я отучился на доктора')
        
    def can_build(self):
        print('Я доктор, я умею строить')
        

class Builder:
    
    def __init__(self, rank):
        self.rank = rank
    
    def graduate(self):
        print('Ура, я отучился на строителя')
    
    def can_build(self):
        print('Я строитель, я умею строить')
        

class Person(Builder, Doctor):
    
    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)
            
    def __str__(self):
        return f"Person {self.rank} {self.degree}"
    
    #def can_build(self):
    #    print('Я человек, я умею строить')
    
print(Person.__mro__)
s = Person('Lok', 'def')
s.graduate()
print(s)