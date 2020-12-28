from re import sub;

def to_digits(s):
    try:
        return int(sub('\D', '', s));
    except ValueError:
        return 0;
