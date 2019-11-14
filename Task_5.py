class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка ручки: {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка карандаша: {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка маркера: {self.title}")


a = Pen("Красная ручка")
b = Pencil("Синий карандаш")

a.draw()
b.draw()
