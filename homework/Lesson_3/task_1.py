"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def div_func(num_1, num_2):
    """
    2 numbers division function
    :param num_1: dividend
    :param num_2: divider
    :return: division result
    """
    try:
        res = float(num_1) / float(num_2)
        return round(res, 2)
    except ZeroDivisionError:
        print("на ноль делить нельзя")
    except ValueError:
        print("вы ввели не число")


print(div_func(input("введите первое число: "), input("введите втрое число: ")))
