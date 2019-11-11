my_dict = {}
hours = 0

with open("text_6.txt", "r") as r:
    for line in r:
        wq = line.replace("(", " ").split()

        for el in wq:
            try:
                hours = hours + int(el)

            except ValueError:
                continue
        my_dict.update({wq[0]: hours})
        hours = 0

print(my_dict)



