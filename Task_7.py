from itertools import count


def my_fun():
    x = 1
    for w in count(2, 1):
        x = x * w
        yield x


i = 1
for el in my_fun():
    if i > 15:
        break
    else:
        print(el)
        i += 1
