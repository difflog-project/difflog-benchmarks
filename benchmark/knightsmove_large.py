input_domains = { 'V' : 256 }
input_relations = {'south' : ['V', 'V'], 'east' : ['V', 'V'], 'se' : ['V', 'V'], 'sw' : ['V', 'V'] }

output_relations = { 'knight' : ['V', 'V'] }

knight = []
for x in range(15):
    for y in range(14):
        knight.append((x + 16 * y, x + 33 + 16 * y))

east = []
for x in range(15):
    for y in range(16):
        east.append((x + 16 * y, x + 1 + 16 * y))

south = []
for x in range(16):
    for y in range(15):
        south.append((x + 16 * y, x + 16 * (y + 1)))

se = []
for x in range(15):
    for y in range(15):
        se.append((x + 16 * y, x + 17 + 16 * y))

sw = []
for x in range(15):
    for y in range(15):
        sw.append((x + 16 * y + 1, x + 16 * (y + 1)))

print east
print south
print se
print sw
print knight


input_tuples = []
output_tuples = []

for x in east:
    input_tuples.append(('east', x[0], x[1]))

for x in south:
    input_tuples.append(('south', x[0], x[1]))

for x in se:
    input_tuples.append(('se', x[0], x[1]))

for x in sw:
    input_tuples.append(('sw', x[0], x[1]))

for x in knight:
    output_tuples.append(('knight', x[0], x[1]))

rules = [
["knight(x,y)","east(x,z)","south(z,y)"],
["knight(x,y)","east(z,x)","south(z,y)"],
["knight(x,y)","east(x,z)","south(y,z)"],
["knight(x,y)","east(z,x)","south(y,z)"],
["knight(x,y)","east(x,z)","east(z,y)"],
['knight(x,y)','east(z,x)','east(z,y)'],
['knight(x,y)','east(x,z)','east(y,z)'],
['knight(x,y)','east(z,x)','east(y,z)'],
['knight(x,y)','east(x,z)','se(z,y)'],
['knight(x,y)','east(z,x)','se(z,y)'],
['knight(x,y)','east(x,z)','se(y,z)'],
['knight(x,y)','east(z,x)','se(y,z)'],
['knight(x,y)','east(x,z)','sw(z,y)'],
['knight(x,y)','east(z,x)','sw(z,y)'],
['knight(x,y)','east(x,z)','sw(y,z)'],
['knight(x,y)','east(z,x)','sw(y,z)'],
['knight(x,y)','south(x,z)','south(z,y)'],
['knight(x,y)','south(z,x)','south(z,y)'],
['knight(x,y)','south(x,z)','south(y,z)'],
['knight(x,y)','south(z,x)','south(y,z)'],
['knight(x,y)','south(x,z)','se(z,y)'],
['knight(x,y)','south(z,x)','se(z,y)'],
['knight(x,y)','south(x,z)','se(y,z)'],
['knight(x,y)','south(z,x)','se(y,z)'],
['knight(x,y)','south(x,z)','sw(z,y)'],
['knight(x,y)','south(z,x)','sw(z,y)'],
['knight(x,y)','south(x,z)','sw(y,z)'],
['knight(x,y)','south(z,x)','sw(y,z)'],
['knight(x,y)','se(x,z)','se(z,y)'],
['knight(x,y)','se(z,x)','se(z,y)'],
['knight(x,y)','se(x,z)','se(y,z)'],
['knight(x,y)','se(z,x)','se(y,z)'],
['knight(x,y)','se(x,z)','sw(z,y)'],
['knight(x,y)','se(z,x)','sw(z,y)'],
['knight(x,y)','se(x,z)','sw(y,z)'],
['knight(x,y)','se(z,x)','sw(y,z)'],
['knight(x,y)','sw(x,z)','sw(z,y)'],
['knight(x,y)','sw(z,x)','sw(z,y)'],
['knight(x,y)','sw(x,z)','sw(y,z)'],
['knight(x,y)','sw(z,x)','sw(y,z)'],
]


true_rules = [
['knight(x,y)','south(x,z)','se(z,y)'],
]

base = 3
chain = None
nc = 1
nl = 1
bound = 20
