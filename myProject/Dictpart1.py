import time
from bisectlist import in_bisect, concatenation1


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def print_hist(h):
    for c in h:
        print(c, h[c])


def histograms_rewrited(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def create_word_dictionary():
    d = dict()
    file = open("words.txt")
    for line in file:
        word = line.strip()
        d[word] = 0
    return d


def word_in_dict(d, s):
    return s in d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_rewrited(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = histograms_rewrited("troncature")
    print_hist(d)
    print(invert_dict(d))
    print(invert_dict_rewrited(d))