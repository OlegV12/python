"""Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexDigit:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return self.re + other.re, self.im + other.im

    def __mul__(self, other):
        return (self.im + self.re) * (other.im + other.re)


a = ComplexDigit(2, 4j)

b = ComplexDigit(3, 5j)

print(a + b)
print(a * b)
