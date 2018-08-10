import math

domains = ['S']

input_relations = {}
input_relations['south'] = ('S', 'S')
input_relations['east'] = ('S', 'S')
input_relations['se'] = ('S', 'S')
input_relations['sw'] = ('S', 'S')

output_relations = {}
output_relations['knight'] = ('S', 'S')

true_rules = ['knight(x, z) :- south(x, y), se(y, z).']

def make_data(n):
    size = int(math.sqrt(n)) + 1

    idb = {}
    edb = {}
    sizes = {}

    sizes['S'] = size * size

    edb['south'] = []
    edb['east'] = []
    edb['se'] = []
    edb['sw'] = []
    south = edb['south']
    east = edb['east']
    se = edb['se']
    sw = edb['sw']

    idb['knight'] = []
    knight = idb['knight']

    for x in range(size - 1):
        for y in range(size - 2):
            knight.append((x + size * y, x + 2 * size + 1 + size * y))

    for x in range(size - 1):
        for y in range(size):
            east.append((x + size * y, x + 1 + size * y))

    for x in range(size):
        for y in range(size - 1):
            south.append((x + size * y, x + size * (y + 1)))

    for x in range(size - 1):
        for y in range(size - 1):
            se.append((x + size * y, x + size + 1 + size * y))

    for x in range(size - 1):
        for y in range(size - 1):
            sw.append((x + size * y + 1, x + size * (y + 1)))

    return (sizes, edb, idb)

if __name__ == "__main__":
    print make_data(32)
