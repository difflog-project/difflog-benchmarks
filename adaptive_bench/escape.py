import random

from difflog import DiffLog
from util import *

domains = ['M', 'V', 'H']

input_relations = {}
input_relations['HFH'] = ('H', 'H')
input_relations['VH'] = ('V', 'H')
input_relations['MmethRet'] = ('M', 'V')
input_relations['MmethArg'] = ('M', 'V')

output_relations = {}
output_relations['rRH'] = ('M', 'H')
output_relations['rMH'] = ('M', 'H')
output_relations['rHH'] = ('H', 'H')

true_rules = [
'rRH(x2:M,x1:H):-MmethRet(x2:M,x0:V),VH(x0:V,x1:H).',
'rRH(x0:M,x2:H):-rHH(x1:H,x2:H),rRH(x0:M,x1:H).',
'rMH(x2:M,x1:H):-MmethArg(x2:M,x0:V),VH(x0:V,x1:H).',
'rMH(x0:M,x2:H):-rHH(x1:H,x2:H),rMH(x0:M,x1:H).',
'rHH(x0:H,x2:H):-HFH(x0:H,x2:H).',
'rHH(x2:H,x1:H):-rHH(x0:H,x1:H),rHH(x2:H,x0:H).',
]

def make_data(n):
    if n < 4:
        n = 4

    edb = {}
    idb = {}
    sizes = {}

    sizes['H'] = n
    sizes['M'] = n
    sizes['V'] = n

    HFH = edb['HFH'] = [(0,1),(1,2),(2,3),(0,2)]
    VH = edb['VH'] = [(1,1),(0,0),(2,2),(3,3)]
    MmethRet = edb['MmethRet'] = [(0,1),(2,1)]
    MmethArg = edb['MmethArg'] = [(0,0),(1,3),(2,2)]

    rMH = idb['rMH'] = [(0,0),(0,1),(0,2),(0,3),(1,3),(2,2),(2,3)]
    rRH = idb['rRH'] = [(0,1),(0,2),(0,3),(2,1),(2,2),(2,3)]
    rHH = idb['rHH'] = [(0,1),(1,2),(2,3),(0,2),(1,3),(0,3)]

    r_HFH = []
    r_VH = []
    r_MmethRet = []
    r_MmethArg = []

    ds = n - 4
    for x in indices_of((ds, ds)):
        if random.random() < 0.1:
            r_HFH.append(x)
    
        if random.random() < 0.1:
            r_VH.append(x)

        if random.random() < 0.1:
            r_MmethRet.append(x)

        if random.random() < 0.1:
            r_MmethArg.append(x)

    d = DiffLog()
    d.add_input_domain("HFH", (ds, ds), r_HFH)
    d.add_input_domain("VH", (ds, ds), r_VH)
    d.add_input_domain("MmethRet", (ds, ds), r_MmethRet)
    d.add_input_domain("MmethArg", (ds, ds), r_MmethArg)

    d.add_result_domain("rMH", (ds, ds), [])
    d.add_result_domain("rRH", (ds, ds), [])
    d.add_result_domain("rHH", (ds, ds), [])

    d.parse_rules_max(true_rules)
    d.eval_program()

    for r in idb:
        for x in d.valuation[r]:
            idb[r].append((x[0] + 4, x[1] + 4))        

    for r in edb:
        for x in d.valuation[r]:
            edb[r].append((x[0] + 4, x[1] + 4))

    return sizes, edb, idb

if __name__ == "__main__":
    print make_data(28)
