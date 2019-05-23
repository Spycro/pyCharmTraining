def readALine(file):
    s = file.readline()
    s.strip()
    print(s)
    return s


def number_of_line(file):
    i = 0
    for line in file:
        i += 1
    return i

def print_over_twenty(file):
    i = 0
    for line in file:
        line = line.strip()
        if has_no_e(line):
            print(line)
            i += 1
    return i


def avoid_in_file(file, forbidden):
    i = 0
    for line in file:
        line = line.strip()
        if avoid(line, forbidden):
            print(line)
            i += 1
    return i


def has_no_e(word):
    for c in word:
        if c == 'e':
            return False
    return True


def avoid(word, forbidden_letter):
    for letter in word:
        if letter in forbidden_letter:
            return False
    return True


def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True


def uses_all(word, charac):
    for letter in charac:
        if letter not in word:
            return False
    return True


def uses_only_in_file(file, uses):
    i = 0
    for line in file:
        line = line.strip()
        if uses_only(line, uses):
            print(line)
            i += 1
    return i


def uses_all_in_file(file, uses):
    i = 0
    for line in file:
        line = line.strip()
        if uses_all(line, uses):
            print(line)
            i += 1
    return i


file = open("words.txt")

forb = input("to be in words character : ")
print(uses_all_in_file(file, forb))
