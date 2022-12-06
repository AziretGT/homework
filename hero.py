class SuperHero:
    people='people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def nHero(self):
        print("Имя герояя", self.name)
    
    def health(self):
        print("Здоровье: ",self.health_points * 2)

    def __str__(self) -> str:
        return f"Status hero:\nПсевдоним - {self.nickname}\nСпособность - {self.superpower}\nЗдоровье - {self.health_points}"
        
    def __len__(self):
        return len(self.catchphrase)

hero=SuperHero("Lana", "Magicion", "Flying", 100, "Give up villian")
hero.nHero()
hero.health()
print(hero)
print(len(hero))
