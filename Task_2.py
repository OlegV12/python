my_list = [1, 2, 3, 4, 5, 6, 7]
list_1 = []
print(my_list)

for i in range(len(my_list)):

    if i % 2 != 0:
        list_1.insert(i - 1, my_list[i])

    else:
        list_1.append(my_list[i])

print(list_1)
