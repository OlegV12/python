with open("text_1.txt", "w") as wr:
    user_input = 0
    while user_input != "":
        user_input = input("введите данные для записи в файл: ")
        print(user_input, file=wr)

