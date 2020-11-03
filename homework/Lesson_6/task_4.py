"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    is_police = False

    def __init__(self, speed, colour, name):
        self.speed = speed
        self.colour = colour
        self.name = name

    def go(self):
        print(f"Car: {self.name} is go")

    def stop(self):
        print(f"Car: {self.name} stopped")

    def turn(self, direction):
        print(f"Car: {self.name} turned {direction}")

    def show_speed(self):
        print(f"Current speed: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f"Current speed: {self.speed}")
        else:
            print("Speed limit exceeded")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f"Current speed: {self.speed}")
        else:
            print("Speed limit exceeded")


class PoliceCar(Car):
    is_police = True


a = TownCar(100, "black", "first car")
b = SportCar(200, "red", "second car")
c = WorkCar(30, "green", "third car")
d = PoliceCar(80, "blue", "police")

a.go()
b.stop()
c.turn("left")
d.go()

a.show_speed()
print(b.name)
c.show_speed()
print(d.is_police)
print(a.is_police)
