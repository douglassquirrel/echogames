from re import sub

def to_digits(s):
    try:
        return int(sub('\D', '', s))
    except ValueError:
        return 0

def first_match(the_list, cond):
    matches = (x for x in the_list if cond(x))
    return next(matches, None)
