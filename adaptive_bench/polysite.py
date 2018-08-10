import random

from difflog import DiffLog
from util import *

domains = ['I', 'C', 'M']

input_relations = {}
input_relations['CICM'] = ('C', 'I', 'M')
input_relations['virtIM'] = ('I', 'M')
input_relations['Mneq'] = ('M', 'M')

output_relations = {}
output_relations['virtI'] = ('I',)
output_relations['polysite'] = ('I',)
output_relations['insvIM'] = ('I', 'M')

true_rules = [
'virtI(x0) :- virtIM(x0, x1).',
'polysite(x3) :- Mneq(x1, x2), insvIM(x3, x1), insvIM(x3, x2).',
'insvIM(x1,x2) :- CICM(x0,x1,x2).'
]

def make_data(n):
    sizes = {}
    edb = {}
    idb = {}

    sizes['I'] = n
    sizes['C'] = 2
    sizes['M'] = n

    CICM = edb['CICM'] = []
    virtIM = edb['virtIM'] = []
    Mneq = edb['Mneq'] = []

    virtI = idb['virtI'] = []
    polySite = idb['polysite'] = []
    insvIM = idb['insvIM'] = []

    ds = n
    for i in range(n - 1):
        for j in range(n - 1):
            if i != j:
                Mneq.append((i+1,j+1))

    for x in indices_of((ds, ds)):
        if random.random() < 0.1:
            if random.random() < 0.5:
                CICM.append((0, x[0], x[1]))
            else:
                CICM.append((1, x[0], x[1]))
    
        if random.random() < 0.1:
            virtIM.append(x)

    d = DiffLog()
    d.add_input_domain("CICM", (2, ds, ds), CICM)
    d.add_input_domain("virtIM", (ds, ds), virtIM)
    d.add_input_domain("Mneq", (ds, ds), Mneq)

    d.add_result_domain("virtI", (ds,), [])
    d.add_result_domain("polysite", (ds,), [])
    d.add_result_domain("insvIM", (ds, ds), [])

    d.parse_rules_max(true_rules)
    d.eval_program()

    for x in d.valuation['insvIM']:
        insvIM.append(x)

    for r in ['polysite', 'virtI']:
        for x in d.valuation[r]:
            idb[r].append(x)

    return sizes, edb, idb

if __name__ == "__main__":
    print make_data(28)
