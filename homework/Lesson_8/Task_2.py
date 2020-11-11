"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data_1 = input("Введите делимое: ")
inp_data_2 = input("Введите делитель: ")

try:
    inp_data_1 = int(inp_data_1)
    inp_data_2 = int(inp_data_2)

    if inp_data_2 == 0:
        raise OwnError("на нуль делить нельзя!")
except OwnError as err:
    print(err)

except ValueError:
    print("вы ввели не число")
else:
    print(round(int(inp_data_1) / int(inp_data_2), 2))
