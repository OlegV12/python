"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_max(iter_obj):
    max_num = iter_obj[0]
    for i in iter_obj:
        if i > max_num:
            max_num = i
    return max_num


def my_func(a_1, a_2, a_3):

    """
    возвращает сумму 2х наибольших чиел
    """

    args_list = [a_1, a_2, a_3]
    try:
        max_1 = my_max(args_list)
        args_list.remove(max_1)
        max_2 = my_max(args_list)
        return max_1 + max_2
    except TypeError:
        print("неправильно задан аргумент")


print(my_func(0, 5.8, 6))


