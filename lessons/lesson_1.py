

class Car:
    # Конструктор класса | Магический метод
    def __init__(self, model, year, color):
        #Атрибуты класса
        self.model = model
        self.year = year
        self.color = color

    def signal(self):
        print(f'{self.color} car signal')

    #Метод класса
    def action(self):
        self.signal()
        return print(f"{self.model} start action")

#Объект класса/ Экземпляр класса
mazda = Car("RX-8", 2004, "red")
bmw = Car('M-5 F90', 2024, 'Black')

mazda.action()
bmw.action()


