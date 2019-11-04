def my_func(x, y):
    z = x * x
    i = 2

    if x == 0:
        print("х не может быть равен 0")
        return

    if abs(y) == 2:
        return 1 / z

    elif y == 0:
        return 1

    else:
        while i != abs(y):
            z = z * x
            i += 1
    return 1 / z


print(my_func(7, -0))
