from itertools import cycle, count

for i in count(5):
    if i > 20:
        break
    else:
        print(i)

z = 0
my_list = [45, 98, 32]
for k in cycle(my_list):
    if z > 10:
        break
    print(k)
    z += 1
