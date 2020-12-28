from random import seed, Random, randrange;
from re import sub;

def to_digits(s):
    return int(sub('\D', '', s));

def nth_random_with_gen(g, min, max, n):
    for _ in range(n):
        r = g.randrange(min, max);
    return r;

def nth_random(the_seed, min, max, n):
    if not isinstance(the_seed, int):
        return nth_random(to_digits(the_seed), min, max, n);
    else:
        return nth_random_with_gen(Random(the_seed), min, max, n);

    
