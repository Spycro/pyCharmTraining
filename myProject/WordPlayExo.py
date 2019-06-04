"""think python 2e Word play case study ex 7 - 9
Author : Lucas Zimmermann
"""


def double(word):
    a=''
    b=''
    for letter in word:
        a = letter
        if a == b:
            return True
        else:
            b = a
    return False


def triple_double(word):
    if len(word)<7:
        return False
    i=1
    while i<len(word):
        if len(word) - i > 6 and word[i]==word[i-1] and word [i+1] == word [i+2] and word[i+3] == word[i+4]:
            return True
        i += 1
    return False


def word_with_triple_double(file):
    i = 0
    for line in file:
        line = line.strip()
        if triple_double(line):
            print(line)
            i += 1
    return i


def is_palindrome(word):
    return word == word[::-1]


def check_miles():
    for i in range(100000, 999996):
        a = str(i)[2:]
        if is_palindrome(a):
            c = i+1
            a = str(c)[1:]
            if is_palindrome(a):
                c = c+1
                a = str(c)[1:5]  # 1 2 3 4 5 6
                if is_palindrome(a):
                    c = c + 1
                    if is_palindrome(str(c)):
                        print(i)

file = open("words.txt")

check_miles()