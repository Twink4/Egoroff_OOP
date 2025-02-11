class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname

        if gender not in ('male', 'female'):
            print('Не знаю, что вы имели в виду? Пусть это будет мальчик!')
            self.gender = 'male'
        else:
            self.gender = gender

    def __str__(self):
        return f"{'Гражданин' if self.gender == 'male' else 'Гражданка'} {self.surname} {self.name}"
