"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(name, surname, b_year, city, email, ph_number):
    print(f"User name: {name}, "
          f"user surname: {surname}, "
          f"user year of birth: {b_year}, "
          f"user city: {city}, "
          f"user email: {email}, "
          f"user phone number: {ph_number}")


u_name = input("input name: ")
u_surname = input("input surname: ")
u_b_year = input("input year of birth: ")
u_city = input("input city: ")
u_email = input("input email: ")
u_ph_number = input("input phone number: ")

user_data(name=u_name, surname=u_surname, b_year=u_b_year, city=u_city, email=u_email, ph_number=u_ph_number)
