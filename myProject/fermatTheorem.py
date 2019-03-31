def check_fermat(a,b,c,n):
    sum1 = pow(a,n) + pow(b,n)
    sum2 = pow (c,n)
    if n>2 and sum1 == sum2 :
        print("Fermat was Wrong")
    else:
        print("no probleme here")


a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
n = int(input("n"))

check_fermat(a,b,c,n)
