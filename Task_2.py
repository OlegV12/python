sec = int(input("введите количество секунд: "))

sec_result = sec % 60
minute = (sec // 60) % 60
hour = (sec // 60) // 60


print(f"{sec} секунд равно: {hour}:{minute}:{sec_result} в формате чч:мм:сс")
