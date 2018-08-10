import random

from difflog import DiffLog
from util import *

domains = ['M', 'I', 'V', 'H', 'F']

input_relations = {}
input_relations['IM'] = ('I', 'M')
input_relations['MI'] = ('M', 'I')
input_relations['VH'] = ('V', 'H')
input_relations['MgetStatFldInst'] = ('M', 'V', 'F')
input_relations['MputStatFldInst'] = ('M', 'F', 'V')
input_relations['MgetInstFldInst'] = ('M', 'V', 'V', 'F')
input_relations['MputInstFldInst'] = ('M', 'V', 'F', 'V')

output_relations = {}
output_relations['rMM'] = ('M', 'M')
output_relations['refStatField'] = ('M', 'F')
output_relations['modStatField'] = ('M', 'F')
output_relations['refInstField'] = ('M', 'H', 'F')
output_relations['modInstField'] = ('M', 'H', 'F')

true_rules = [
'rMM(x0M,x1M) :- rMM(x0M,x2M),rMM(x2M,x1M).',
'rMM(x0M,x1M) :- IM(x2I,x1M),MI(x0M,x2I).',
'refStatField(x0M,x1F) :- rMM(x0M,x2M),refStatField(x2M,x1F).',
'refStatField(x0M,x1F) :- MgetStatFldInst(x0M,x2V,x1F).',
'modStatField(x0M,x1F) :- rMM(x0M,x2M),modStatField(x2M,x1F).',
'modStatField(x0M,x1F) :- MputStatFldInst(x0M,x1F,x2V).',
'refInstField(x0M,x1H,x2F) :- rMM(x0M,x3M),refInstField(x3M,x1H,x2F).',
'refInstField(x0M,x1H,x2F) :- MgetInstFldInst(x0M,x3V,x4V,x2F),VH(x4V,x1H).',
'modInstField(x0M,x1H,x2F) :- MputInstFldInst(x0M,x3V,x2F,x4V),VH(x3V,x1H).',
'modInstField(x0M,x1H,x2F) :- modInstField(x3M,x1H,x2F),rMM(x0M,x3M).',
]

def make_data(n):
    if n < 8:
        n = 8

    edb = {}
    idb = {}
    sizes = {}

    sizes['M'] = n
    sizes['V'] = n
    sizes['H'] = n
    sizes['I'] = n
    sizes['F'] = n

    MgetInstFldInst = edb['MgetInstFldInst'] = [(4,3,2,2)]
    MputInstFldInst = edb['MputInstFldInst'] = [(4,4,3,5)]
    MgetStatFldInst = edb['MgetStatFldInst'] = [(4,0,0),(5,6,4),(7,6,6)]
    MputStatFldInst = edb['MputStatFldInst'] = [(4,1,1),(6,5,7),(7,6,7)]
    VH = edb['VH'] = [(2,2),(4,4)]
    MI = edb['MI'] = [(0,0), (1,1), (2,2), (3,3)]
    IM = edb['IM'] = [(0,1), (1,2), (2,3), (3,4)]

    rMM = idb['rMM'] = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
    refStatField = idb['refStatField'] = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,4),(7,6)]
    modStatField = idb['modStatField'] = [(0,1),(1,1),(2,1),(3,1),(4,1),(6,5),(7,6)]
    refInstField = idb['refInstField'] = [(0,2,2),(1,2,2),(2,2,2),(3,2,2),(4,2,2)]
    modInstField = idb['modInstField'] = [(0,4,3),(1,4,3),(2,4,3),(3,4,3),(4,4,3)]

    r_MgetInstFldInst = []
    r_MputInstFldInst = []
    r_MgetStatFldInst = []
    r_MputStatFldInst = []
    r_VH = []
    r_MI = []
    r_IM = []

    ds = n - 8
    for x in indices_of((ds, ds)):
        if random.random() < 0.1:
            r_IM.append(x)

        if random.random() < 0.1:
            r_MI.append(x)

        if random.random() < 0.1:
            r_VH.append(x)


    for x in indices_of((ds,ds,ds)):
        if random.random() < 0.01:
            r_MputStatFldInst.append(x)

        if random.random() < 0.01:
            r_MgetStatFldInst.append(x)

    for x in indices_of((ds,ds,ds,ds)):
        if random.random() < 0.001:
            r_MputInstFldInst.append(x)

        if random.random() < 0.001:
            r_MgetInstFldInst.append(x)
        
    d = DiffLog()
    d.add_input_domain("MI", (ds,ds), r_MI)
    d.add_input_domain("IM", (ds,ds), r_IM)
    d.add_input_domain("VH", (ds,ds), r_VH)
    d.add_input_domain("MputStatFldInst", (ds,ds,ds), r_MputStatFldInst)
    d.add_input_domain("MgetStatFldInst", (ds,ds,ds), r_MgetStatFldInst)
    d.add_input_domain("MputInstFldInst", (ds,ds,ds,ds), r_MputInstFldInst)
    d.add_input_domain("MgetInstFldInst", (ds,ds,ds,ds), r_MgetInstFldInst)

    d.add_result_domain("rMM", (ds,ds), [])
    d.add_result_domain("refStatField", (ds,ds), [])
    d.add_result_domain("modStatField", (ds,ds), [])
    d.add_result_domain("refInstField", (ds,ds,ds), [])
    d.add_result_domain("modInstField", (ds,ds,ds), []) 

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
