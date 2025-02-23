class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating
        
    

    def __eq__(self, value):
        if isinstance(value, int):
            return self.rating == value
        elif isinstance(value, ChessPlayer):
            return self.rating == value.rating
        else:
            return "Невозможно выполнить сравнение"
        
        
    def __gt__(self, value):
        ...


magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)  # False
print(ian == 2789)  # True
