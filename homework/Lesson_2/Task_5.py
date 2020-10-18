"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

rating = [7, 5, 3, 3, 2, 1]
print(rating)

while True:
    user_number = input("Введите новый элемент рейтинга(q для выхода): ")
    if user_number == "q":
        print(f'Рейтинг:\n{rating}\nпрограмма завершена')
        break
    else:
        user_number = int(user_number)
        if user_number in rating:
            rating.insert(rating.index(user_number) + rating.count(user_number), user_number)
        else:
            rating.append(user_number)
        print(rating)
