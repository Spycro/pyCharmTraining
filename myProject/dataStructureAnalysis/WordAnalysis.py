import string
from carTalkTuple import _make_word_list

def strip_line(line):
    line = line.replace('-', ' ')
    res = line.split()

    for i in range(len(res)):
        res[i] = res[i].strip(string.punctuation + string.whitespace)
        res[i] = res[i].lower()
    return res


def make_word_analysis(book):
    d = dict()
    word_list = []
    for line in book:
        word_list.extend(strip_line(line))
    for word in word_list:
        d[word] = d.get(word, 0) +1
    d.pop('')
    return d


def print_first_twenty(d):
    l = list()
    for key in d:
        l.append((d[key],key))
    l.sort(reverse=True)
    for i in range(20):
        print(l[i])


def print_word_not_in_book(book_dict, word_dict):
    for key in book_dict:
        if key not in word_dict:
            print(key)


if __name__ == '__main__':
    fin = open("books1.txt")
    word_frequency = make_word_analysis(fin)
    print_first_twenty(word_frequency)
    word_list = _make_word_list()

    print_word_not_in_book(word_frequency, word_list)

