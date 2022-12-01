class SuperHero:
    people="people"
    def __init__(self,name, nickname, superpower, health_points, catchphrase):
        self.name=name
        self.nickname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase
    def __str__(self):
        return f'Имя героя: {self.name}\n'\
               f'Псевдоним героя: {self.nickname}\n'\
               f'Суперсила героя: {self.superpower}\n'\
               f'Очки здоровья героя: {self.health_points*2}\n'\
               f'Коронная фраза героя: {self.catchphrase}, в коронной фразе героя {len(self.catchphrase)} букв'

hero=SuperHero("Lana", "Magician", "Flying",500, "Give up vilian!!!")
print(hero)
