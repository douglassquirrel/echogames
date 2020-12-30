from random import Random, randrange
from util import n_times

def nth_random_with_gen(g, min, max, n):
    return n_times(n, lambda : g.randrange(min, max))

def nth_random(the_seed, min, max, n):
    return nth_random_with_gen(Random(the_seed), min, max, n)

    
