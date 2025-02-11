class Vector:
    def __init__(self, *args):
        self.nums_list = sorted(el for el in args if type(el) is int)
        
        
    def __str__(self):
        return f"Вектор{tuple(self.nums_list)}"\
        if len(self.nums_list)\
        else "Пустой вектор"