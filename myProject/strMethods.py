def is_palindrome(word):
    return word == word[::-1]



while True:
    a = input()
    if is_palindrome(a):
        print(a +" is a palidrome")
    else:
        print(a + " is not a palindrome")