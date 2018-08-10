import random

from difflog import DiffLog
from util import *

domains = ['V', 'H', 'C', 'F', 'M', 'Z']

input_relations = {}
input_relations['points_initial'] = ('V', 'H')
input_relations['load'] = ('V', 'F', 'V')
input_relations['store'] = ('V', 'F', 'V')
input_relations['assign'] = ('C', 'V', 'C', 'V')
input_relations['invocation'] = ('C', 'H', 'C', 'M')
input_relations['actual'] = ('H', 'Z', 'V')
input_relations['formal'] = ('M', 'Z', 'V')

output_relations = {}
output_relations['pointsto'] = ('C', 'V', 'H')
output_relations['heappointsto'] = ('H', 'F', 'H')

true_rules = [
'pointsto(x2C,x0V,x1H) :- invocation(x2C,x1H,x3C,x4M),points_initial(x0V,x1H).',
'pointsto(x2C,x3V,x1H) :- assign(x2C,x3V,x4C,x0V),points_initial(x0V,x1H).',
'pointsto(x0C,x1V,x2H) :- heappointsto(x5H,x4F,x2H),load(x3V,x4F,x1V),pointsto(x0C,x3V,x5H).',
'heappointsto(x0H,x1F,x2H) :- pointsto(x5C,x3V,x0H),pointsto(x5C,x4V,x2H),store(x3V,x1F,x4V).',
]

def make_data(n):
    if n < 12:
        n = 12

    sizes = {}
    edb = {}
    idb = {}

    sizes['H'] = n
    sizes['Z'] = 5
    sizes['F'] = n / 4
    sizes['V'] = n
    sizes['C'] = n / 3
    sizes['M'] = 5

    original_sizes = {}
    original_sizes['H'] = 12
    original_sizes['Z'] = 3
    original_sizes['F'] = 3
    original_sizes['C'] = 4
    original_sizes['V'] = 12
    original_sizes['M'] = 3

    points_initial = edb['points_initial'] = [(1,1),(2,2),(5,1),(9,9),(11,11)]
    load = edb['load'] = [(2,2,8),(5,1,10),(5,1,7)]
    assign = edb['assign'] = [(2,5,1,5),(2,7,1,7),(2,5,3,6),(2,7,3,2)]
    store = edb['store'] = [(7,2,5),(5,1,1),(9,2,5),(9,1,11)]
    invocation = edb['invocation'] = [(1,1,2,1),(3,2,2,1),(2,9,1,1),(3,11,1,1)]
    actual = edb['actual'] = [(1,0,5),(1,1,7),(2,0,6),(2,1,2)]
    formal = edb['formal'] = [(1,0,5),(1,1,7),(2,0,3),(2,1,6)]

    pointsto = idb['pointsto'] = [(1,1,1),(1,5,1),(3,2,2),(3,11,11),(2,9,9),(2,5,1),(2,7,2),(1,10,1),(1,7,1),(2,7,1),(3,8,1),(2,10,1)]
    heappointsto = idb['heappointsto'] = [(1,1,1),(2,2,1),(1,2,1),(9,2,1)]

    r_load = []
    r_store = []
    r_points_initial = []
    r_assign = []
    r_invocation = []
    r_actual = []
    r_formal = []

    ds = n - 12
    for x in indices_of((ds, 2, ds)):
        if random.random() < 0.1:
            r_store.append(x)
            store.append((x[0] + 12, x[1] + 3, x[2] + 12))
    
        if random.random() < 0.1:
            r_load.append(x)
            load.append((x[0] + 12, x[1] + 3, x[2] + 12))

    for x in indices_of((ds, ds)):
        if random.random() < 0.1:
            r_points_initial.append(x)
            points_initial.append((x[0] + 12, x[1] + 12))

    for x in indices_of((ds, 2, ds)):
        if random.random() < 0.01:
            formal_rand = random.randint(0,1)

            r_actual.append(x)
            r_formal.append((formal_rand, x[1], x[2]))

            actual.append((x[0] + 12, x[1] + 3, x[2] + 12))
            formal.append((formal_rand + 3, x[1] + 3, x[2] + 12))

    for x in indices_of((ds / 3, ds, ds/3, 2)):
        if random.random() < 0.1:
            r_invocation.append(x)
            invocation.append((x[0] + 4, x[1] + 12, x[2] + 4, x[3] + 3))

    for x in indices_of((ds / 3, ds, ds/3, ds)):
        if random.random() < 0.01:
            r_assign.append(x)
            assign.append((x[0] + 4, x[1] + 12, x[2] + 4, x[3] + 12))

    d = DiffLog()
    d.add_input_domain("points_initial", (ds, ds), r_points_initial)
    d.add_input_domain("load", (ds, 2, ds), r_load)
    d.add_input_domain("store", (ds, 2, ds), r_store)
    d.add_input_domain("assign", (ds/3, ds, ds/3, ds), r_assign)
    d.add_input_domain("invocation", (ds/3, ds, ds/3, 2), r_invocation)
    d.add_input_domain("actual", (ds, 2, ds), r_actual)
    d.add_input_domain("formal", (2, 2, ds), r_formal)

    d.add_result_domain("pointsto", (ds/3, ds, ds), [])
    d.add_result_domain("heappointsto", (ds, 2, ds), [])

    d.parse_rules_max(true_rules)
    d.eval_program()

    for x in d.valuation['heappointsto']:
        heappointsto.append((x[0] + 12, x[1] + 3, x[2] + 12))

    for x in d.valuation['pointsto']:
        pointsto.append((x[0] + 4, x[1] + 12, x[2] + 12))

    return sizes, edb, idb

if __name__ == "__main__":
    print make_data(28)
