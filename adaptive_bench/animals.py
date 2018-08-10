from difflog import DiffLog

domains = ['A', 'C']

input_relations = {}
input_relations['feathers'] = ('C',)
input_relations['hair'] = ('C',)
input_relations['scales'] = ('C',)
input_relations['none'] = ('C',)
input_relations['has_milk'] = ('A',)
input_relations['homeothermic'] = ('A',)
input_relations['has_eggs'] = ('A',)
input_relations['has_gills'] = ('A',)
input_relations['has_covering'] = ('A', 'C')

output_relations = {}
output_relations['mammal'] = ('A',)
output_relations['fish'] = ('A',)
output_relations['reptile'] = ('A',)
output_relations['bird'] = ('A',)


true_rules = ['bird(x) :- feathers(y), has_covering(x,y).'
             ,'fish(x) :- has_gills(x).'
             ,'mammal(x) :- has_covering(x,y),has_milk(x).'
             ,'reptile(x) :- has_covering(x,y),scales(y).']

def make_data(n):
    idb = {}
    edb = {}
    sizes = {}

    sizes['C'] = 4
    sizes['A'] = n

    edb['feathers'] = [(0,)]
    edb['hair'] = [(1,)]
    edb['scales'] = [(2,)]
    edb['none'] = [(3,)]
    
    has_milk = edb['has_milk'] = []
    homeothermic = edb['homeothermic'] = []
    has_eggs = edb['has_eggs'] = []
    has_gills = edb['has_gills'] = []
    has_covering = edb['has_covering'] = []

    mammal = idb['mammal'] = []
    fish = idb['fish'] = []
    reptile = idb['reptile'] = []
    bird = idb['bird'] = []

    for x in range(n):
        if x % 4 == 0:
            mammal.append((x,))
            has_milk.append((x,))
            homeothermic.append((x,))
            has_covering.append((x, 1))
        elif x % 4 == 1:
            fish.append((x,))
            has_gills.append((x,))
            has_eggs.append((x,))
        elif x % 4 == 2:
            reptile.append((x,))
            has_covering.append((x, 2))
            has_eggs.append((x,))
        else:
            bird.append((x,))
            homeothermic.append((x,))
            has_covering.append((x, 0))
            has_eggs.append((x,))

    return (sizes, edb, idb)
