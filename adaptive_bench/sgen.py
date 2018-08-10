from difflog import DiffLog

domains = ['P']

input_relations = {}
input_relations['parent'] = ('P', 'P')

output_relations = {}
output_relations['sgen'] = ('P', 'P')

true_rules = ['sgen(x0,x1) :- parent(x0,x2),parent(x1,x2).'
             ,'sgen(x0,x3) :- parent(x0,x1),sgen(x1,x2),parent(x3,x2).']

def make_data(n):
    idb = {}
    edb = {}
    sizes = {}

    edb['parent'] = []
    idb['sgen'] = []

    parent = edb['parent']
    sgen = idb['sgen']

    if n % 2 == 0:
        n += 1

    sizes['P'] = n

    lasts = (1, 2)
    parent.append((1,0))
    parent.append((2,0))
    for i in range(n/2 - 1):
        parent.append((lasts[0] + 2, lasts[0]))
        parent.append((lasts[1] + 2, lasts[1]))
        lasts = (lasts[0] + 2, lasts[1] + 2)

    evaluator = DiffLog()
    evaluator.parse_rules_max(true_rules)
    evaluator.add_input_domain('parent', (n, n), parent)
    evaluator.add_result_domain('sgen', (n, n), [])

    evaluator.eval_program()

    for r in idb:
        for x in evaluator.valuation[r]:
            idb[r].append(x)

    return (sizes, edb, idb)


