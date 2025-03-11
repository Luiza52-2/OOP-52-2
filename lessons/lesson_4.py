from curses import wrapper


# staticmethod (статический метод) — это метод, который не требует доступа к экземпляру или
# классу. Он ведет себя как обычная функция, но внутри класса.



class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

# print(MathUtils.add(1,4))



# classmethod (метод класса) — это метод, который получает доступ к самому классу, а не к его экземплярам.



class Person:

    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1


    @classmethod
    def get_count(cls):
        return cls.count

    def test(self):
        pass


p1 = Person("Alice")
p2 = Person("John")
p3 = Person("Oleg")


# print(Person.get_count())




class Person:


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @property
    def test(self):
        return f"{self.first_name} {self.last_name}"


    @test.setter
    def test(self, value):
        first, last = value.split()
        self.first_name = first
        self.last_name = last



# p = Person("John", "Doe")
# print(p.test)
# p.test = "Ardager Dev"
# print(p.first_name)
# print(p.last_name)


# Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию в качестве аргумента и возвращает
# измененную или новую функцию. Они позволяют добавлять новую функциональность к существующим
# функциям без изменения их кода.


# Пример простого декоратора

def my_decorator(func):   # 3

    def wrapper():   # %
        print("Перед выполнением функции") # 6
        func() # 7
        print('После выполнением функции') # 9

    return wrapper # 4


@my_decorator
def hello():               # 2
    print("Привет") # 8


# hello() # 1


# Декораторы с аргументами

def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator


# amount = int(input("ведите количество"))

# @repeat(amount)
# def greet():
#     print("привет!!!")


# greet()




# Декораторы для классов


def class_decorator(cls):

    class NewClass(cls):

        def new_method(self):
            return print("Новый метод!!")
    return NewClass


@class_decorator
class MyClass:

    def old_method(self):
        return print("Старый метод")


obj = MyClass()

obj.old_method()
obj.new_method()