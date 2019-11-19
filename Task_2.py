from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def calc(self):
        return f"на пошив пальто нужно: {round(self.size / 6.5 + 0.5 , 2)}м. материала"


class Costume(Clothes):

    @property
    def calc(self):
        return f"на пошив костюма нужно: {round(self.size * 2 + 0.3, 2)}м. материала"


a = Coat(43)
b = Costume(48)

print(a.calc())
print(b.calc)
