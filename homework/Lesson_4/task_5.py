"""Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def my_reduce(func, lst):
    if len(lst) == 2:
        return func(lst[0], lst[1])
    else:
        lst[0] = func(lst[0], lst[1])
        lst.pop(1)
        return my_reduce(func, lst)


def my_range(start=0, stop=0, step=1):
    i = start
    res = []
    while i < stop:
        res.append(i)
        i += step

    return res


def m_func(a, b):
    return a * b


new_list = [el for el in my_range(100, 1001) if el % 2 == 0]

print(new_list)
print(reduce(m_func, new_list))  # reduce func (just to check)

print(my_reduce(m_func, new_list))  # my_reduce func
