"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = input("please input numbers separating them with space: ").split()
list_1 = []
print(my_list)

for i in range(len(my_list)):

    if i % 2 != 0:
        list_1.insert(i - 1, my_list[i])

    else:
        list_1.append(my_list[i])

print(list_1)

print("-" * 20)

for itm in range(1, len(my_list), 2):
    my_list[itm - 1], my_list[itm] = my_list[itm], my_list[itm - 1]

print(my_list)
