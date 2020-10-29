"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

counter = 0
new_list = []
with open("text_5.txt", "w") as r:
    while counter != 10:
        new_list.append(str(randint(1, 100)))
        counter += 1
        str_list = ",".join(new_list)
    r.write(str_list)
print(f"Числа сохраненные в файле text_5.txt: {str_list.split(',')}")

with open("text_5.txt", "r") as f:
    result = 0
    for line in f:
        my_list = line.split(",")

        for number in my_list:
            result = result + int(number)
print(f"Сумма чисел в файле text_5.txt: {result}")
