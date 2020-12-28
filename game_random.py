from random import seed, Random, randrange;

def nth_random_with_gen(g, min, max, n):
    for _ in range(n):
        r = g.randrange(min, max);
    return r;

def nth_random(the_seed, min, max, n):
    return nth_random_with_gen(Random(the_seed), min, max, n);

    
