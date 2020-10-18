"""
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

list_of_items = []
names_list = []
price_list = []
amount_list = []
count_list = []
i = 1
while True:

    x = input("Добавить товар? Y/N: ")
    if x == "Y":
        name = input("Введите название товара: ")
        price = int(input("Введите цену товара: "))
        amount = int(input("Введите количество: "))
        count = input("Введите единицу измерения: ")
        list_of_items.append((i, {"Название": name,
                                  "Цена": price,
                                  "Количество": amount,
                                  "ед": count, }))
        i += 1
        names_list.append(name)
        price_list.append(price)
        amount_list.append(amount)
        count_list.append(count)

    else:
        break
d = dict(list_of_items)
new_dict = {"Название": names_list, "Цена": price_list, "Количество": amount_list, "ед.": count_list}

print(list_of_items)
print(new_dict)
