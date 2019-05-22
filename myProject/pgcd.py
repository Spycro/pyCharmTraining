

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


while True:
    a = int(input())
    b = int(input())
    print(str(gcd(a, b)))
