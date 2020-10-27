"""Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def my_enumerate(some_list, start=0):
    """
    enumerate function analog
    :param some_list:
    :param start:
    :return: generator
    """
    while start < len(some_list):
        for item in some_list:
            yield start, item
            start += 1


my_list = [32, 1453, 123, 12, 432, 124, 300, 440, 450, 0, 12]

new_list = [el for i, el in my_enumerate(my_list) if el > my_list[i - 1]]

print(new_list)
