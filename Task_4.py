g = input("Введите слова через пробел: ")

my_list = g.split(" ")
for ind, i in enumerate(my_list, 1):
    print(ind, i[:10])




