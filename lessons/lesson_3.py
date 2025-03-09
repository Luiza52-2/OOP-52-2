# Инкапсуляция
# def some(self): - Открытый метод
# def _some(self): - Закрытый метод
# def __some(self): - Приватный метод

#  self.some - Открытый атрибут
#  self._some(self): - Закрытый атрибут
#  self.__some(self): - Приватный атрибут


class BankAccount:

    def __init__(self, username, balance, pin_code):
        self.username = username
        self._balance = balance
        self.__pin_code = pin_code

    def deposit(self, amount):
        if amount > 0:
            self.__to_up_balance(amount)
            return print(f" Баланс {self.username} пополнен на {amount}. \n Текущий баланс {self._balance}")
        else:
            return print("Сумма должна быть положительной")

    def __to_up_balance(self, amount):
        self._balance += amount

    def get_balance(self, pin_code):
        if self.__pin_code == pin_code:
            return print(f"Ваш Баланс: {self._balance}")
        else:
            return print("не верный пин-код")

user1 = BankAccount("Ardager", 1000, 1234)

# print(user1._balance)
# print(user1._BankAccount__pin_code)
# print(dir(user1))

# user1.get_balance(1234)
# user1.deposit(100)


# Абстракция

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass # Определяет интерфейс для звука

    @abstractmethod
    def move(self):
        pass # Определяет интерфейс для движения



class Dog(Animal):


    def make_sound(self):
        return print("Gaf gaf")


    def move(self):
        return print("moving")


gufi = Dog()

gufi.make_sound()
gufi.move()



# Nikita - RuSms - Twilio - UZSms


class SmsServiceAbc(ABC):

    @abstractmethod
    def send_sms(self):
        pass
