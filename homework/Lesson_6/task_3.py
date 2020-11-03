"""Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"employee full name: {self.name}  {self.surname}")

    def get_total_income(self):
        print(f"Total income: {self.income.get('wage') + self.income.get('bonus')}")


a = Position("Ivan", "Petrov", "Engineer", 100, 300)
a.get_total_income()
a.get_full_name()
print(a.income)
print(a.position)
print(a.name)

b = Position("Sergey", "Ivanov", "Supervisor", 300, 200)
b.get_total_income()
b.get_full_name()
print(b.income)
print(b.position)
print(b.name)
