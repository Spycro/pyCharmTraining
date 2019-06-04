
def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if word == "":
        return True
    elif last(word) == first(word):
        return is_palindrome(middle(word))
    else:
        return False


while True:
    a = input()
    if is_palindrome(a):
        print(a + " is a palidrome")
    else:
        print(a + " is not a palindrome")