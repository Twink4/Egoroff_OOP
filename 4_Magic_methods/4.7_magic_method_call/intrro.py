from time import perf_counter
class Counter:
    
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print("Init", self)
        
    def __call__(self, *args, **kwds):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f"Объект вызывался {self.counter} раз.")
        
    def average(self):
        return self.summa / self.length 
       
class Timer:
    def __init__(self, func):
        self.fn = func
        
    def __call__(self, *args, **kwds):
         start = perf_counter()
         print(f"Вызывалась функция {self.fn.__name__}")
         result = self.fn(*args, **kwds)
         end = perf_counter()
         print(f"Функция отработала за {end - start}")
         return result
     
     
@Timer
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

f = Timer(fib)
print(f(34))

print(fact(5))