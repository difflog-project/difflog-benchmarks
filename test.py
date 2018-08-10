import importlib
from difflog import DiffLog

tests = ['ancestor', 'andersen', 'animals', 'callsite_1' 'escape', 'knights_move', 'path', 'polysite', 'sgen']

broken = ['modref']

def test_module(s):
    benchmark = importlib.import_module("adaptive_bench.{}".format(s))
    (size, edb, idb) = benchmark.make_data(20)

    d = DiffLog()
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

    # compare result and edb

if __name__ == "__main__":
    for x in tests:
        print x
        test_module(x)
