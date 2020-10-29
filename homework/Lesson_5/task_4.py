"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_list = ["Один", "Два", "Три", "Четыре"]
with open("text_4s.txt", "r") as f, \
        open("text_4r.txt", "w") as w:
    for line, word in zip(f, my_list):
        my_line = line.split()
        my_line.pop(0)
        my_line.insert(0, word)
        print(','.join(map(str, my_line)).replace(',', " "), file=w)
