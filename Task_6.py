

def int_func(arg):
    return arg.title()


g = input("Input words: ").split(" ")
my_str = []
for i in g:
    my_str.append(int_func(i))

print(' '.join(my_str))

