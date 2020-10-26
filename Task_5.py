from random import randint
n = 0
new_list = []
with open("text_5.txt", "w") as r:
    while n != 10:
        new_list.append(str(randint(1, 100)))
        n += 1
        z = ",".join(new_list)
    r.write(z)
print(f"Числа сохраненные в файле text_5.txt: {z.split(',')}")

with open("text_5.txt", "r") as f:
    result = 0
    for line in f:
        q = line.split(",")
        for number in q:
            result = result + int(number)
print(f"Сумма чисел в файле text_5.txt: {result}")

