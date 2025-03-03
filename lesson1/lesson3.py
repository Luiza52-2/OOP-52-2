#Дикомпозиция проекта_ Наследование, инкапсуляция.

#Родительский класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        return  print(f'Я {self.name}, мой уровень {self.lvl}')

    def action(self):
        return print(f'{self.name} выполнчет базовое действие')

# warrior = Hero('Kirito', 100, 1000)


#Дочерний класс
class Warrior(Hero):

    def __init__(self, name, lvl, hp, st):
        super().__init__(name, lvl, hp)
        self.st = st


    def attact(self):
        if self.st >= 10:
            self.st -= 1
            return print(f'{self.name} атакует мечом!')
        else:
            return print(f'{self.name} мало стомины!!')

    def introduce(self):
        return print(f' Name: {self.name} ST: {self.st}')

class MagaHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp


kirito = Warrior('Kirito', 100, 1000, 10)
gandalf_hero = MagaHero('Gandalf', 100, 1000, 10)

kirito.action()
kirito.introduce()
kirito.attact()

kirito.action()
kirito.introduce()


#Полиморфизм
