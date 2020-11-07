"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

from random import randint


class Matrix:
    length = 3  # длина строки матрицы
    height = 3  # количество строк матрицы
    numbers = []

    """функция заполнения матрицы случайными целыми числами от 0 до 100"""

    def fill_numbers(self):
        numbers = []
        self.numbers = numbers
        i = 0
        while i != Matrix.length * Matrix.height:
            self.numbers.append(str(randint(0, 100)))
            i += 1

    def __str__(self):
        i = 0
        while i <= Matrix.length * Matrix.height:
            print(f"{' '.join(self.numbers[i:i + Matrix.length])}")
            i += Matrix.length
        return "---"

    def __add__(self, other):
        result_list = []
        for el_1, el_2 in zip(self.numbers, other.numbers):
            result_list.append(str(int(el_1) + int(el_2)))
        a = Matrix()
        a.numbers = result_list
        return a


q = Matrix()
q.fill_numbers()
print(q)

b = Matrix()
b.fill_numbers()
print(b)

print(q + b)
