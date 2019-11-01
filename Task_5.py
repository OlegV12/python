rating = [7, 5, 3, 3, 2, 1]
print(rating)

while True:
    s = input("Желаете ввести элемент рейтинга? Y/N: ")
    if s == "Y":
        x = int(input("Введите новый элемент рейтинга: "))
        for i in rating:
            ind = rating.index(i)

            if i > x:
                if ind == len(rating) - 1:
                    rating.append(x)
                    print(rating)
                    break

                continue

            else:
                ind = rating.index(i)
                rating.insert(ind, x)
                print(rating)
                break
    else:
        break
print(rating)

