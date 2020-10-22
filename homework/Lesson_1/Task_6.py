"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

start_km = int(input("Введите количество километров в 1й день: "))
finish_km = int(input("Введите целевое значение километров: "))
days = 1
delta_km = start_km

while delta_km <= finish_km:
    delta_km = delta_km * 1.1
    # для вывода ежедневного результата - раскомментировать
    # print(delta_km)
    days += 1

print(f"Целевое значение километров будет достигнуто на {days}-й день")
