
s_km = int(input("Введите количество километров в 1й день: "))
f_km = int(input("Введите целевое значение километров: "))
days = 1
d_km = s_km

while d_km <= f_km:
    d_km = d_km * 1.1
    print(d_km)
    days = days + 1

print(f"Целевое значение километров будет достигнуто на {days}-й день")
