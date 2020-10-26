

def my_func(a_1, a_2, a_3):

    """
    возвращает сумму 2х наибольших чиел
    """

    f = [a_1, a_2, a_3]
    try:
        max_1 = max(f)
        f.remove(max_1)
        max_2 = max(f)
        return max_1 + max_2
    except TypeError:
        print("неправильно задан аргумент")


print(my_func(0, 5.8, 6))
