
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"employee full name: {self.name}  {self.surname}")

    def get_total_income(self):
        print(f"Total income: {self._income.get('wage') + self._income.get('bonus')}")


a = Position("Ivan", "Petrov", "Engineer", 100, 300)
a.get_total_income()
a.get_full_name()
print(a._income)
print(a.position)
print(a.name)

b = Position("Sergey", "Ivanov", "Supervisor", 300, 200)
b.get_total_income()
b.get_full_name()
print(b._income)
print(b.position)
print(b.name)
