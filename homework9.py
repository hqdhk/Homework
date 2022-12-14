# Напишите программу с классом Car. Создайте конструктор (__init__) класса Car. Создайте атрибуты класса Car — color (цвет), type (тип),
# year (год). Напишите три метода для этого класса. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий - магический метод str  для вывода атрибутов экземпляра
# в виде строки.

class Car:
    def __init__(self, type, color, date):
        self.type = type
        self.color = color
        self.date = date
    def engine_on(self):
        return f"{self.type} {self.color} {self.date} engine on"

    def engine_off(self):
        return f"{self.type} {self.color} {self.date} engine off"

    def __str__(self):
        return f"{self.type} {self.color} {self.date}"



car_1 = Car(type="Audi TT", color="Yellow", date=2016)
car_2 = Car(type="BMW M5", color="Blue", date=2015)
car_3 = Car(type="MB S500", color="Black", date=2012)


print(car_2)
