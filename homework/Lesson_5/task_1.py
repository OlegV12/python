"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("text_1.txt", "w", encoding="UTF-8") as file:
    user_input = 0
    while user_input != "":
        user_input = input("введите данные для записи в файл: ")
        print(user_input, file=file)
