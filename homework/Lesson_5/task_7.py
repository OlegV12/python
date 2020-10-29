"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

a_prof = 0
result_dict = {}
aver_dict = {}
my_list = [result_dict, aver_dict]
firm_count = 0
with open("text_7s.txt", "r") as r:
    for line in r:
        my_line = line.split()
        profit = int(my_line[2]) - int(my_line[3])
        result_dict.update({my_line[0]: profit})
        if profit >= 0:
            a_prof = a_prof + profit
            firm_count += 1
        aver_dict.update({"average_profit": round((a_prof / firm_count), 2)})

print(my_list)

with open("text_7res.txt", "w", encoding="UTF-8") as j_file:
    json.dump(my_list, j_file, ensure_ascii=False)
