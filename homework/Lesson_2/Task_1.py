"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
my_list = [1, 45, "name", 32.23, True, {"value": 329}]

for ind, i in enumerate(my_list, 1):
    print(ind, i, type(i))
