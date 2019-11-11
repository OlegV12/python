g = ["Один", "Два", "Три", "Четыре"]
with open("text_4s.txt", "r") as f, \
        open("text_4r.txt", "w") as w:
    for line, k in zip(f, g):
        m = line.split()
        m.pop(0)
        m.insert(0, k)
        print(','.join(map(str, m)).replace(',', " "), file=w)
