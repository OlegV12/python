
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

user_month = int(input("Введите месяц:"))

# реализация через list

if user_month in winter:
    print("Зима")
elif user_month in spring:
    print("Весна")
elif user_month in summer:
    print("Лето")
elif user_month in autumn:
    print("Осень")
else:
    print("Ошибка")

# реализация через dict

my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
           10: "Осень", 11: "Осень", 12: "Зима"}
print(my_dict.get(user_month))
