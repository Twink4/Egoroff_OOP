class Building:
    
    def __init__(self, count: int):
        self.companies: list[dict] = [{"name": None} for _ in range(count)]
        
    def __setitem__(self, etage: int, value):
        self.companies[etage]["name"] = value
        
    def __delitem__(self, etage):
        self.companies[etage]["name"] = None
    
    def __getitem__(self, etage):
        return self.companies[etage]["name"]
    
iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])