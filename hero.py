class SuperHero:
    people='people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase,fly=False):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.fly= fly
    def nHero(self):
        print("Имя герояя", self.name)
    
    def health(self):
        print("Здоровье: ",self.health_points * 2)

    def __str__(self) -> str:
        return f"Status hero:\nПсевдоним - {self.nickname}\nСпособность - {self.superpower}\nЗдоровье - {self.health_points}"
        
    def __len__(self):
        return len(self.catchphrase)

    def fly():
        return "hh"    


hero=SuperHero("Lana", "Magician", "Super_Jump", 100, "Give up villian")
hero.nHero()
hero.health()
print(hero)
print(len(hero))


class IceHero(SuperHero):
    icecontrol="Icecontrol-can control ice."

    def health(self):
        self.fly=fly=True
        print("Здоровье: ",self.health_points ** 2)

    def fly_phrase(self):
        print("fly in the True_phrase")
        

ice_hero=IceHero("Articuno", "Ice bird", "Telepathy", 12, "Quuu")
print(ice_hero)
ice_hero.health()
ice_hero.fly_phrase()
print()


class FireHero(SuperHero):
    firecontrol="Firecontrol-can control fire."
    def health(self):
        self.fly=fly=True
        print("Здоровье: ",self.health_points ** 2)

    def fly_phrase(self):
        print("fly in the True_phrase")

fire_hero=FireHero("Moltres", "Fire bird", "Physic", 11, "Quu uu")
print(fire_hero)
fire_hero.health()
fire_hero.fly_phrase()
print()


class ThunderHero(SuperHero):
    thundercontrol="Thundercontrol- can control thunder."
    def health(self):
        self.fly=fly=True
        print("Здоровье: ",self.health_points ** 2)

    def fly_phrase(self):
        print("fly in the True_phrase")

thunder_hero=ThunderHero("Zapdos", "Thunder bird", "Agility", 10, "Quu Qu")
print(fire_hero)
thunder_hero.health()
thunder_hero.fly_phrase()

