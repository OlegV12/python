"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_number = int(input("введите число: "))
result = 0
number = user_number
while number > 0:
    last_digit = number % 10
    if last_digit >= result:
        result = last_digit
        if last_digit == 9:
            break
    number = number // 10

print(f"наиболшая цифра в вашем числе {user_number}: {result}")
