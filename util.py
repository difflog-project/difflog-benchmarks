import itertools

def indices_of(t):
    to_return = []
    for i in t:
        to_return.append(list(range(i)))
    return itertools.product(*to_return)

