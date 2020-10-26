
def my_func(*args):

    """
    возвращает сумму введенных чисел
    """

    my_list = []
    args = input("Please input numbers for sum (input 'q' to quit):").split(' ')
    print(f"you input: {args}")
    if 'q' in args:
        args.remove('q')
        for i in args:
            try:
                i = float(i)
                my_list.append(i)
            except ValueError:
                continue
    else:
        for i in args:
            try:
                i = float(i)
                my_list.append(i)
            except ValueError:
                continue

    return round(sum(my_list), 2)


print(my_func())

