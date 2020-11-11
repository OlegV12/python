"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def my_method(cls, date):
        cls.date = date

        day, month, year = cls.date.split("-")
        return int(day), int(month), int(year)

    @staticmethod
    def check_method(date):
        day, month, year = date.split("-")
        try:
            if 1 > int(day) or int(day) > 31:
                print("day error")
            if 1 > int(month) or int(month) > 12:
                print("month error")
            if int(year) < 0:
                print("year error")
        except ValueError:
            print("value error")


z = Date("11-11-11")
print(z.my_method("11-11-11"))

print(Date.my_method("22-22-22"))

Date.check_method("q-0-00")

z.check_method("45-0-00")
