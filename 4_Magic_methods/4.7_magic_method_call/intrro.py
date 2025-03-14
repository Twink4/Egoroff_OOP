import random
class Counter:
    
    def __init__(self):
        self.counter = 0
        print("Init", self)
        
    def __call__(self, *args, **kwds):
        self.counter += 1
        print(f"Объект вызывался {self.counter} раз.")
       
        
trry = Counter()

for _ in range(random.randint(0, 1000)):
    trry()