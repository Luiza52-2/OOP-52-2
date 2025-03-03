#Класс Hero
class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP
    def introduce(self):
        print(f'Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}.')

    def is_adult(self):
        return self.lvl >=10

hero1 = Hero('Миранда', 5, 100)
hero2 = Hero('Мария', 12, 120)
hero3 = Hero('Иван', 10, 150)

heroes = [hero1, hero2, hero3]

for hero in heroes:
    hero.introduce()
    print(f'{hero.name} взрослый? {hero.is_adult()}')
    print()


