from sys import argv

script_name, hours, h_pay, bonus = argv
print(f' salary = {(int(hours) * int(h_pay)) + int(bonus)}')
