import random

from difflog import DiffLog
from util import *

domains = ['H']

input_relations = {}
input_relations['load'] = ('H', 'H')
input_relations['assgn'] = ('H', 'H')
input_relations['addr'] = ('H', 'H')
input_relations['store'] = ('H', 'H')

output_relations = {}
output_relations['pt'] = ('H', 'H')

true_rules = [
'pt(x0,x1) :- addr(x0,x1).',
'pt(x2,x1) :- assgn(x2,x0), pt(x0,x1).',
'pt(x3,x1) :- load(x3,x2), pt(x0,x1), pt(x2,x0).',
'pt(x3,x1) :- store(x2,x0), pt(x0,x1), pt(x2,x3).',
]

def make_data(n):
    if n < 8:
        n = 8

    sizes = {}
    edb = {}
    idb = {}

    sizes['H'] = n

    load = edb['load'] = [(7, 2)]
    assgn = edb['assgn'] = [(4, 1)]
    addr = edb['addr'] = [(1, 2), (2, 3), (3, 5), (5, 6)]
    store = edb['store'] = [(4, 5)]

    pt = idb['pt'] = [(1, 2), (2, 3), (3, 5), (5, 6), (4, 2), (7, 5), (2, 6)]

    r_load = []
    r_store = []
    r_addr = []
    r_assgn = []

    ds = n - 8
    for x in indices_of((ds, ds)):
        if random.random() < 0.02:
            r_store.append(x)
    
        if random.random() < 0.02:
            r_load.append(x)

        if random.random() < 0.04:
            r_addr.append(x)

        if random.random() < 0.04:
            r_assgn.append(x)

    d = DiffLog()
    d.add_input_domain("store", (ds, ds), r_store)
    d.add_input_domain("load", (ds, ds), r_load)
    d.add_input_domain("addr", (ds, ds), r_addr)
    d.add_input_domain("assgn", (ds, ds), r_assgn)

    d.add_result_domain("pt", (ds, ds), [])

    d.parse_rules_max(true_rules)
    d.eval_program()

    for r in idb:
        for x in d.valuation[r]:
            idb[r].append((x[0] + 8, x[1] + 8))        

    for r in edb:
        for x in d.valuation[r]:
            edb[r].append((x[0] + 8, x[1] + 8))

    return sizes, edb, idb

if __name__ == "__main__":
    print make_data(28)
