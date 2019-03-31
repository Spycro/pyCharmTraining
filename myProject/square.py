import numpy as np
def sqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return y


def test_sqrt():
    print('a'.ljust(3)+''+'sqrt'.ljust(25)+''+'np.sqrt'.ljust(25)+''+'diff')
    for i in range(1,10):
        a = sqrt(i)
        b = np.sqrt(i)
        print(str(i).ljust(3)+''+str(a).ljust(25)+''+str(b).ljust(25)+''+str(b-a))


test_sqrt()