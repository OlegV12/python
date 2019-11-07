
from functools import reduce


def m_func(a, b):
    return a * b


new_list = [el for el in range(100, 1001) if el % 2 == 0]

print(new_list)
print(reduce(m_func, new_list))
