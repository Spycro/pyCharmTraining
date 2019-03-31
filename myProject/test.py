import math


def volumesphere(r):
    a = (4/3)*math.pi*pow(r,3)
    print(a)


def right_justify(s):
    print(' '*70 + s)


def do_twice(f, s):
    f(s)
    f(s)


def do_four(f,s):
    do_twice(f,s)
    do_twice(f,s)


def print_tak(s):
    print(s)


do_four(print_tak, 'tak')