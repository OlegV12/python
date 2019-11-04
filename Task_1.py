
def div_func(a_1, a_2):

    """
    возвращает результат деления a_1 на a_2
    """

    try:
        res = float(a_1) / float(a_2)
        return round(res, 2)
    except ZeroDivisionError:
        print("на ноль делить нельзя")
    except ValueError:
        print("вы ввели не число")


print(div_func(input("введите первое число: "), input("введите втрое число: ")))