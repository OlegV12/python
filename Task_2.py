with open("text_2.txt", "r") as f:
    line_count = 0
    for line in f:
        line_count += 1
        print(line, f"Эта строка содержит: {len(line.split())} слов(а).")

print(f"всего сторк в файле: {line_count} ")