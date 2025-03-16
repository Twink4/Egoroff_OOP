class Vector:
    def __init__(self, *args):
        self.values = list(args)
    
    def __repr__(self):
        return str(self.values)