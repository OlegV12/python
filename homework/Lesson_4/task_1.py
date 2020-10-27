"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hours, h_pay, bonus = argv
try:
    print(f' salary = {(int(hours) * int(h_pay)) + int(bonus)}')
except ValueError:
    print('Введите часы, ставку и премию')
