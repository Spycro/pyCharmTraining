def word_minus_letter(word, i):
    word_as_list = list(word)
    word_as_list.pop(i)
    return ''.join(word_as_list)


def word_children(word, d):
    l = list()
    for i in range(len(word)):
        if word_minus_letter(word, i) in d:
            l.append(word_minus_letter(word, i))
    return l


def _make_word_list():
    d = dict()
    file = open("words.txt")
    for line in file:
        word = line.strip()
        d[word] = None
    d["i"] = None
    d["a"] = None
    d[""] = None
    return d

memo = dict()

def is_reducible(word, d):
    if word == '':
        return True
    word_child = word_children(word, d)
    if len(word_child) > 0:
        for each_word in word_child:
            if each_word in memo or is_reducible(each_word, d):
                memo[each_word] = None
                return True
    else:
        return False


def find_reducible_word(d):
    l = list()
    for word in d:
        if is_reducible(word, d):
            print(word)
            l.append((len(word), word))
    l.sort(reverse=True)
    return l


word_dict = _make_word_list()
word_dict_test = {"print" : None, "prit" : None, "prt" : None, "pt" : None, "p" : None, "trastbourg": None, "":None }
my_list = find_reducible_word(word_dict)
print(my_list[0][1])