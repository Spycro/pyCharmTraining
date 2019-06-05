import random


def nested_sum(alist):
    a = 0
    for l in alist:
        a += sum(l)
    return a


def cumsum(alist):
    sum = 0
    t = []
    for i in alist:
        sum += i
        t.append(sum)
    return t


def middle(alist):
    t = alist[1:-1]
    return t


def chop(alist):
    alist.pop()
    alist.pop(0)


def is_sorted(alist):
    for i in range(1,len(alist)):
        if alist[i-1] > alist[i]:
            return False
    return True


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        for c in str1:
            if c not in str2:
                return False
            else:
                str2 = str2.replace(c, "", 1)
    return True


def has_duplicate(alist):
    for i in range(len(alist)):
        if alist[i] in alist[i+1:]:
            return True
    return False


def birthday_estimate(nb_simulation):
    c = 0
    for i in range(nb_simulation):
        t = []
        for people in range(23):
            t.append(random.randint(1,365))
        if has_duplicate(t):
            c += 1
    print((c/nb_simulation)*100)


birthday_estimate(100000)
