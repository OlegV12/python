
def div_func(a_1, a_2):
    try:
        res = a_1 / a_2
        return res
    except ZeroDivisionError:
        print("на ноль делить нельзя")


print(round(div_func(float(input("введите первое число: ")), float(input("введите втрое число: "))), 2))