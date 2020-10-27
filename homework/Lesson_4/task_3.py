"""Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""


def my_range(start=0, stop=0, step=1):
    i = start
    res = []
    while i < stop:
        res.append(i)
        i += step

    return res


my_list = [i for i in my_range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(my_list)
