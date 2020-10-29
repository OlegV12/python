"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

employees = 0
salary = 0
low_salary = []
with open("text_3.txt", "r") as f:
    for line in f:
        a = line.split()
        salary = salary + float(a[1])
        employees += 1
        if float(a[1]) < 20000:
            low_salary.append(a[0])

print(f"Средняя зарплата на предприятии: {round(salary / employees, 2)}")
print(f"Сотрудники с запплатой ниже 20000: {', '.join(low_salary)}")
