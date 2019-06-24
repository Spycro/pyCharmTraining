import string
import random


def text_to_string(s):
    return open(s).read()

def markov_analysis(book_title, n = 2):
    text_to_analyse = text_to_string(book_title)
    text_to_analyse = text_to_analyse.replace('-',' ')
    text_in_table = text_to_analyse.split()
    d = dict()
    for i in range(len(text_in_table) - n):
        t = [text_in_table[i+k] for k in range(n)]
        try:
            d.setdefault(tuple(t), []).append(text_in_table[i+n])
        except IndexError:
            print(i, n, i+n, len(text_in_table))
    return d


def generate_text(markov_dict, how_many_word = 50):
    s = " "
    s = s.join(random.choice(list(markov_dict.keys())))
    for i in range(how_many_word):
        two_last_words = s.split()[len(s.split()) - 2:]
       # print(markov_dict.get(tuple(two_last_words)), two_last_words)
        s = s + " " +  str(random.choice(markov_dict.get(tuple(two_last_words))))
        #print(s)
    return s



emmma_dict = markov_analysis("../emma.txt")
print(generate_text(emmma_dict))