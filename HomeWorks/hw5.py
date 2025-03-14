class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Прямоугольник (ширина: {self.x}, высота: {self.y})'
    def area(self):
        return self.x * self.y

    def __eq__(self,other):
        return self.area() == other.area()
    def __lt__(self, other):
        return self.area() < other.area()
    def __gt__(self, other):
        return self.area() > other.area()


r1 = Rectangle(4, 5)  # Прямоугольник шириной 4 и высотой 5
r2 = Rectangle(3, 6)  # Прямоугольник шириной 3 и высотой 6

print(r1)  # Должен вывести: Прямоугольник (ширина: 4, высота: 5)
print(r2)  # Должен вывести: Прямоугольник (ширина: 3, высота: 6)

print(r1.area())  # Должно вывести: 20 (4 * 5)
print(r2.area())  # Должно вывести: 18 (3 * 6)

print(r1 == r2)  # Должно вывести: False (20 != 18)
print(r1 > r2)  # Должно вывести: True (20 > 18)
print(r1 < r2)  # Должно вывести: False (20 < 18)