class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return print(f'{self.name} выполняет действие.')

    def attack(self):
        return print(f'{self.name} атакует противника.')

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            success = "успешно" if self.precision > 50 else "неудачно"
            return print(f'{self.name} стреляет из лука. Атака {success}. Осталось стрел {self.arrows}')
        else:
            return print(f'{self.name} не может атаковать - стрелы закончились!')

    def rest(self):
        self.arrows += 5
        return print(f'{self.name} отдыхает и пополняет запас стрел. Теперь у него {self.arrows} стрел.')

    def status(self):
        return print(f'Герой {self.name}: Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}%')

if __name__ == "__main__":
    hero = Heroes('Воин', 100)
    archer = Archer("Лучник", 80, 10, 60)

    hero.action()
    hero.attack()

    archer.attack()
    archer.rest()
    archer.status()