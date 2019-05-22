def is_divisible(a, b):
    if a<b:
        return False
    elif a%b == 0:
        return True
    else:
        return False

def is_power(a,b):
    if a == 1:
        return True
    elif is_divisible(a, b):
        return is_power(a/b, b)
    else:
        return False


while True:
    a = int(input())
    b = int(input())
    if is_power(a,b):
        print(str(a) +" is a power of "+ str(b))
    else:
        print(str(a) + " is not a power of " + str(b))
