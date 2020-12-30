from math import copysign
from re import sub

def to_digits(s):
    try:
        return int(sub('\D', '', s))
    except ValueError:
        return 0

def flatten(L):
    return [item for sublist in L for item in sublist]

def sign(x):
    return 0 if x == 0 else int(copysign(1, x))

def compare(a, b):
    return sign(a - b)

def n_times(n, L):
    for _ in range(n):
        r = L()
    return r;
