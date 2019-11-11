import json
a_prof = 0
result_dict = {}
aver_dict = {}
my_list = [result_dict, aver_dict]
firm_count = 0
with open("text_7s.txt", "r") as r:
    for line in r:
        f = line.split()
        profit = int(f[2]) - int(f[3])
        result_dict.update({f[0]: profit})
        if profit >= 0:
            a_prof = a_prof + profit
            firm_count += 1
        aver_dict.update({"average_profit": round((a_prof / firm_count), 2)})

print(my_list)

with open("text_7res.txt", "w") as j_file:
    json.dump(my_list, j_file, ensure_ascii=False)

