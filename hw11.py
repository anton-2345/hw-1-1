h = int(input("Высота треугольника"))
for i in range(h):
    symb = "*" * (1+2*i)
    space = " " * (h-i-1)
    print(space + symb)