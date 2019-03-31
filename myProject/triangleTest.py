def is_triangle(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print("no")
    else:
        print("Yes")


a = int(input("a\n"))
b = int(input("b\n"))
c = int(input("c\n"))

is_triangle(a, b, c)
