from difflog import DiffLog

domains = ['P']

input_relations = {}
output_relations = {}

output_relations['parent'] = ('P', 'P')
output_relations['ancestor'] = ('P', 'P')

input_relations['father'] = ('P', 'P')
input_relations['mother'] = ('P', 'P')

true_rules = ['parent(x,y) :- father(x,y).'
             ,'parent(x,y) :- mother(x,y).'
             ,'ancestor(x,y) :- parent(x,y).'
             ,'ancestor(x,z) :- parent(x,y),ancestor(y,z).']


def make_data(n):
    if n % 2 == 0:
        n += 1

    idb = {}
    edb = {}
    sizes = {}
    
    sizes['P'] = n

    edb['father'] = []
    father = edb['father']
    edb['mother'] = []
    mother = edb['mother']

    male = False
    last = 0
    for i in range(n/2):
        father.append((last + 1, last))
        mother.append((last + 2, last))
        
        if male:
            last = last + 1
        else: 
            last = last + 2

        male = not male

    idb['parent'] = []
    parent = idb['parent']
    idb['ancestor'] = []
    ancestor = idb['ancestor']

    evaluator = DiffLog()
    evaluator.parse_rules_max(true_rules)
    evaluator.add_input_domain('father', (n, n), father)
    evaluator.add_input_domain('mother', (n, n), mother)
    evaluator.add_result_domain('parent', (n, n), [])
    evaluator.add_result_domain('ancestor', (n, n), [])

    evaluator.eval_program()

    for r in idb:
        for x in evaluator.valuation[r]:
            idb[r].append(x)
            
    return (sizes, edb, idb)

