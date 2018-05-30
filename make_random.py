import importlib
import itertools
import random
import sys

def indices_of(m, arr):
    to_return = []
    for i in arr:
        to_return.append(list(range(m.input_domains[i])))
    return itertools.product(*to_return)

def inject_noise(m, rate):
    for (r, d) in m.output_relations.items():
        new_tuples = []
        for i in indices_of(m, d):
            if random.random() < rate:
                new_tuples.append(i)

        sys.stderr.write(str(new_tuples))    
        for n in new_tuples:
            new = [r] + list(n)
            if new in m.output_tuples:
                m.output_tuples.remove(new)
            else:
                m.output_tuples.append(new)


if __name__ == "__main__":
    benchmark = importlib.import_module("benchmark.andersen")
    inject_noise(benchmark, 0.01)
