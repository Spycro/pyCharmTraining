def anagram(file):
    d = dict()
    for line in file:
        word = line.strip()
        t = tuple(sorted(word))
        d.setdefault(t, []).append(word)

    to_remove = list()
    for key in d:
        if len(d[key]) < 2:
            to_remove.append(key)

    for key in to_remove:
        d.pop(key)

    return d


def print_dict(d):
    for key in d:
        print(key, " : ", d[key])


def print_dict_by_order(d):
    t = set()
    for key in d:
        t.add(len(d[key]))

    for i in range(max(t), 0, -1):
        for key in d:
            if len(d[key]) == i:
                print(d[key], " : ", key)


def bingo(d, n):
    s = set()
    for key in d:
        if len(key) == n:
            s.add(len(d[key]))

    for key in d:
        if len(d[key]) == max(s) and len(key) == n:
            print(d[key], " : ", key)


def differ_by_two_letter(word1, word2):
    """Check if two words differ by two letter
    word1 ,word2 : strings on same length
    """
    i=0
    for c1,c2 in zip(word1, word2):
        if c1 != c2:
            i += 1
    return i == 2


def metathesis_pair(d):
    """Find all metathesis pair as desribe in think python 2e on tuple exercise 2
    d: a dictionnary of anagram , with character tuple as key"""
    l = list()
    for key in d:
        for word1 in d[key]:
            for word2 in d[key]:
                if word1<word2 and differ_by_two_letter(word1, word2):
                    l.append((word1, word2))
    return l


if __name__ == '__main__':
    f = open("words.txt")
    anagram_dict = anagram(f)
    print(metathesis_pair(anagram_dict))

