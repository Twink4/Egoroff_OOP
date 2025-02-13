class Ingredient:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name}: {self.weight}г."


class Pizza:
    def __init__(self, name, ingredients=None):
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    def __str__(self):
        lst = "\n".join(f"{i.name}: {i.weight}г." for i in sorted(
            self.ingredients, key=lambda x: x.weight, reverse=True))
        return f"Пицца {self.name} состоит из:\n{lst}"


tomatoes = Ingredient('tomatoes', 200)
cheese = Ingredient('mozzarella', 400)
print(tomatoes)
print(cheese)

peperoni = Pizza('Пеперони')
peperoni.ingredients.append(tomatoes)
peperoni.ingredients.append(cheese)
print(peperoni)
