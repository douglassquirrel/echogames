from math import copysign
from re import sub

def to_digits(s):
    try:
        return int(sub('\D', '', s))
    except ValueError:
        return 0

def first_match(the_list, cond):
    matches = (x for x in the_list if cond(x))
    return next(matches, None)

def flatten(L):
    return [item for sublist in L for item in sublist]

def sign(x):
    return 0 if x == 0 else int(copysign(1, x))

def compare(a, b):
    return sign(a - b)
