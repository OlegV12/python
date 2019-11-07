
my_list = [32, 1453, 123, 12, 432, 124, 12, 12, 34, 43, 43]

res_list = [el for el in my_list if my_list.count(el) < 2]

print(my_list)

print(res_list)
