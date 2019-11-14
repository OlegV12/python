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

