domains = ['N']

input_relations = {}
input_relations['edge'] = ('N', 'N')

output_relations = {}
output_relations['path'] = ('N', 'N')


true_rules = ['path(x,y) :- edge(x,y).'
             ,'path(x,z) :- edge(x,y),path(y,z).']

def make_data(n):
    edb = {}
    idb = {}
    sizes = {}

    sizes['N'] = n

    edb['edge'] = []
    for i in range(n - 1):
        edb['edge'].append((i,i+1))

    idb['path'] = []
    for i in range(n):
        for j in range(i):
            idb['path'].append((j,i))

    return (sizes, edb, idb)
