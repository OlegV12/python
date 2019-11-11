employees = 0
salary = 0
low_salary = []
with open("text_3.txt", "r") as f:

    for line in f:
        m = line.split()
        salary = salary + float(m[1])
        employees += 1
        if float(m[1]) < 20000:
            low_salary.append(m[0])

print(f"Средняя зарплата на предприятии: {round(salary / employees, 2) }")
print(F"Сотрудники с запплатой ниже 20000: {', '.join(low_salary)}")