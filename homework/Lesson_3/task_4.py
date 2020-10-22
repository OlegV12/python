"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return "Вы ввели неверные аргументы"
    return result


def my_range(start=0, stop=0, step=1):
    i = start
    res = []
    while i < stop:
        res.append(i)
        i += step

    return res


def my_another_func(x, y):
    try:
        x, y = float(x), int(y)
        result = x
        for i in my_range(0, abs(y) - 1):
            result *= x
        return 1/result
    except ValueError:
        return 'ValueError'


print(my_another_func(4.5, -4))
print(my_func(4.5, -4))






