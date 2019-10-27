
u = int(input("введите число: "))
result = 0
while u // 10 != 0:
    z_1 = u % 10
    z_2 = (u // 10) % 10

    if z_1 >= z_2:
        if result <= z_1:
            result = z_1
    else:
        if result <= z_2:
            result = z_2
    u = u // 10
print(f"наиболшая цифра в вашем числе: {result}")