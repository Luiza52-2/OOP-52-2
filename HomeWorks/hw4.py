# Декоратор преобразующий результат в верхний регистр
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def say_hello():
    return "Привет!"
print(say_hello())
