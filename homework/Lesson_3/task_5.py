"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_sum(some_list):
    result = 0
    for i in some_list:
        result += i
    return result


def some_func(*args):
    result = 0
    while True:
        user_list = input("Please input numbers for sum (input 'q' to quit):").split(" ")

        if 'q' in user_list:
            user_list.remove('q')
            try:
                result_list = [int(i) for i in user_list]
            except TypeError:
                return 'Type Error'
            result += my_sum(result_list)
            return result
        else:
            try:
                result_list = [int(i) for i in user_list]
                result += my_sum(result_list)
                print(f'intermediate sum: {result}')
            except TypeError:
                return 'Type Error'
            except ValueError:
                return 'ValueError'


print(some_func())
