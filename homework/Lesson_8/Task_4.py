"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class Storage:
    def __init__(self):
        self.my_dict = {"total USD": 0}

    def storage_in(self, obj, number):
        try:
            if obj.model in self.my_dict:
                self.my_dict.update({obj.model: self.my_dict[obj.model] + number})
                self.my_dict.update({"total USD": self.my_dict["total USD"] + obj.price * number})
            else:
                self.my_dict.update({obj.model: number, "total USD": self.my_dict["total USD"] + obj.price * number})
        except TypeError:
            print('TypeError')

    def storage_out(self, obj, number):
        try:
            if obj.model in self.my_dict:
                if self.my_dict[obj.model] - number < 0:
                    print(f"на складе нет столько {obj.name}")
                self.my_dict.update({obj.model: self.my_dict[obj.model] - number})
                self.my_dict.update({"total USD": self.my_dict["total USD"] - obj.price * number})
        except TypeError:
            print('TypeError')


class OfficeEquipment:
    def __init__(self, model, price):
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, model, price):
        super().__init__(model, price)


class Scanner(OfficeEquipment):
    def __init__(self, model, price):
        super().__init__(model, price)


class Xerox(OfficeEquipment):
    def __init__(self, model, price):
        super().__init__(model, price)


scanner = Scanner("ScannerModel3", 100)
xerox = Xerox("xerox1", 300)
printer = Printer("Print1", 200)
scanner2 = Scanner("ScannerModel2", 150)
store = Storage()

store.storage_in(scanner2, 10)
store.storage_in(xerox, 3)
store.storage_in(scanner, 1)
store.storage_in(printer, 5)
print(store.my_dict)
store.storage_in(scanner2, 5)
store.storage_out(printer, 2)
print(store.my_dict)
store.storage_out(printer, 1)
print(store.my_dict)

store.storage_in(scanner2, "три")
