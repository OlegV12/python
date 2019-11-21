class Storage:
    def __init__(self):
        self.my_dict = {"total USD": 0}

    def storage_in(self, obj, number):
        if obj.model in self.my_dict:
            self.my_dict.update({obj.model: self.my_dict[obj.model] + number})
            self.my_dict.update({"total USD": self.my_dict["total USD"] + obj.price * number})
        else:
            self.my_dict.update({obj.model: number, "total USD": self.my_dict["total USD"] + obj.price * number})

    def storage_out(self, obj, number):
        if obj.model in self.my_dict:
            if self.my_dict[obj.model] - number < 0:
                print(f"на складе нет столько {obj.name}")
            self.my_dict.update({obj.model: self.my_dict[obj.model] - number})
            self.my_dict.update({"total USD": self.my_dict["total USD"] - obj.price * number})


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



s = Scanner("S3", 100)
x = Xerox("x1", 300)
p = Printer("P1", 200)
r = Scanner("r2", 150)
store = Storage()

store.storage_in(r, 10)
store.storage_in(x, 3)
store.storage_in(s, 1)
store.storage_in(p, 5)
print(store.my_dict)
store.storage_in(r, 5)
store.storage_out(p, 2)
print(store.my_dict)
store.storage_out(p, 1)
print(store.my_dict)


