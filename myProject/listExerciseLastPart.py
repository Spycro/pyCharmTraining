import time

def concatenation1():
    t = []
    file = open("words.txt")
    for line in file:
        word = line.strip()
        t.append(word)
    return t


def concatenation2():
    t = []
    file = open("words.txt")
    for line in file:
        word = line.strip()
        t = t + [word]
    return t


tps = time.time()
t = concatenation1()
tpsTotal = time.time() - tps

print(tpsTotal, len(t))

tps = time.time()
t = concatenation2()
tpsTotal = time.time() - tps

print(tpsTotal)
