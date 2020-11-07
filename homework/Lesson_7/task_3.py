"""Реализовать программу работы с клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
умножение (mul()), деление (truediv()). Данные методы должны выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
В классе необходимо реализовать метод make_cell(), принимающий экземпляр класса и количество клеток в ряду.
Метод должен возвращать строку виду **\n\n**..., где количество клеток между \n равно переданному аргументу,
а количество рядов определяется, исходя из общего количества клеток.
При создании экземпляра клетки должна происходить перезапись параметра, который хранит количество клеток.
"""


class Cage:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cage(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cage(self.cells - other.cells)
        else:
            return f"Разница не является положительным числом"

    def __mul__(self, other):
        return f"{Cage(self.cells * other.cells)}"

    def __truediv__(self, other):
        return Cage(round(self.cells / other.cells))

    def __str__(self):
        return f"({self.cells})"

    def make_order(self, raw):
        i = 0
        while i != self.cells // raw:
            print(f"{'*' * raw}")
            i += 1
        print(f"{'*' * (self.cells % raw)}")


a = Cage(10)
b = Cage(8)
c = Cage(22)

print(a + b)
print(a - b)
print(a - c)
print(a * b)
print(a / b)
a.make_order(3)
b.make_order(3)
c.make_order(5)
