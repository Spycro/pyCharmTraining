import bisect


def in_bisect(sortedlist, target):
    if len(sortedlist) == 0:
        return False
    i = len(sortedlist) // 2
    a = sortedlist[i]
    if a == target:
        return True
    if target < a:
        return in_bisect(sortedlist[:i], target)
    else:
        return in_bisect(sortedlist[i + 1:], target)


def concatenation1():
    t = []
    file = open("words.txt")
    for line in file:
        word = line.strip()
        t.append(word)
    return t


def reverse_search():
    t = concatenation1()
    answer = []
    for word in t:
        if in_bisect(t, word[::-1]):
            answer.append(word)
    print(answer)


def interlock_search():
    word_list = concatenation1()
    answer = []
    for word in word_list:
        word1 = word[::2]
        word2 = word[1::2]
        if in_bisect(word_list, word1) and in_bisect(word_list, word2):
            answer.append([word, word1, word2])
        if len(answer) == 300:
            print(answer)
            return None
    print(answer)

if __name__ == '__main__':
    interlock_search()
