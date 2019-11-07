

my_list = [32, 1453, 123, 12, 432, 124, 300, 440, 450, 0, 12]


new_list = [el for i, el in enumerate(my_list) if el > my_list[i-1]]

print(new_list)
