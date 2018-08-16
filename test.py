import importlib
import numpy as np
from difflog import DiffLog

tests = ['ancestor', 'andersen', 'animals', 'callsite_1', 'escape', 'knights_move', 'path', 'polysite', 'sgen']

tests = ['modref']

def add_data(benchmark, d, size, edb, idb):
    for x in benchmark.input_relations:
        dims = []
        for dim in benchmark.input_relations[x]:
            dims.append(size[dim])
        
        d.add_input_domain(x, dims, edb[x])

    for x in benchmark.output_relations:
        dims = []
        for dim in benchmark.output_relations[x]:
            dims.append(size[dim])

        d.add_result_domain(x, dims, [])

def test_correctness(s, n):
    benchmark = importlib.import_module("adaptive_bench.{}".format(s))
    (size, edb, idb) = benchmark.make_data(n)

    d = DiffLog()
    add_data(benchmark, d, size, edb, idb)

    d.parse_rules_max(benchmark.true_rules)
    d.eval_program()

    for x in benchmark.input_relations:
        for t in edb[x]:
            if t not in d.valuation[x]:
                print d.valuation[x].keys()
                print edb[x]
                print x
                assert(False)

        for t in d.valuation[x]:
            if t not in edb[x]:
                print d.valuation[x].keys()
                print edb[x]
                print x
                assert(False)

    for x in benchmark.output_relations:
        for t in idb[x]:
            if t not in d.valuation[x]:
                print d.valuation[x].keys()
                print idb[x]
                print x
                print edb
                assert(False)

        for t in d.valuation[x]:
            if t not in idb[x]:
                assert(False)

def test_usefulness(s, n):
    benchmark = importlib.import_module("adaptive_bench.{}".format(s))
    (size, edb, idb) = benchmark.make_data(n)

    d = DiffLog()
    add_data(benchmark, d, size, edb, idb)
    d.parse_rules_max(benchmark.true_rules)
    d.eval_program()

    all_useful = True
    for r in benchmark.true_rules:
        y = benchmark.true_rules[:]
        y.remove(r)
        
        removed = DiffLog()
        add_data(benchmark, removed, size, edb, idb)
        d.parse_rules_max(benchmark.true_rules)

        good = False
        for x in benchmark.output_relations:
            if not good:
                for t in d.valuation[x]:
                    if t not in removed.valuation[x]:
                        good = True
                        break

        if not good:
            all_useful = False
            print "{} not useful".format(r)
        else:
            print "{} useful".format(r)

    return all_useful

def test_degenerate(s, n):
    benchmark = importlib.import_module("adaptive_bench.{}".format(s))
    (size, edb, idb) = benchmark.make_data(n)

    d = DiffLog()
    add_data(benchmark, d, size, edb, idb)
    d.parse_rules_max(benchmark.true_rules)
    d.eval_program()

    for x in benchmark.output_relations:
        if np.array_equal(d.relation_map[x], np.ones(d.relation_map[x].shape)):
            print "{} degenerate".format(x)
            return False

    return True


if __name__ == "__main__":
    test_usefulness('andersen', 20)
    test_degenerate('andersen', 20)
    #for x in tests:
    #    print x
    #    test_module(x, 20)
