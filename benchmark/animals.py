input_domains = {'A' : 21, 'C' : 4 }
input_relations = {'feathers': ['C'], 'scales': ['C'],
                   'hair': ['C'], 'none': ['C'], 'has_covering': ['A', 'C'],
                   'has_milk': ['A'], 'homeothermic': ['A'], 'has_eggs': ['A'],
                   'has_gills': ['A']}
output_relations = {'mammal': ['A'], 'fish': ['A', 'A'],
                    'reptile': ['A'], 'bird': ['A', 'A']}

input_tuples = [
    ['feathers', 0], ['scales', 1], ['hair', 2], ['none', 3],
    ['has_covering', 0, 2], ['has_covering', 1, 3], ['has_covering', 2, 2],
    ['has_covering', 3, 2], ['has_covering', 4, 3], ['has_covering', 5, 3],
    ['has_covering', 6, 3], ['has_covering', 7, 3], ['has_covering', 8, 1],
    ['has_covering', 9, 1], ['has_covering', 10, 1], ['has_covering', 11, 1],
    ['has_covering', 12, 1], ['has_covering', 13, 0], ['has_covering', 14, 0],
    ['has_covering', 15, 0], ['has_milk', 0], ['has_milk', 1], ['has_milk', 2],
    ['has_milk', 3], ['has_milk', 16], ['homeothermic', 0], ['homeothermic', 1],
    ['homeothermic', 2], ['homeothermic', 3], ['homeothermic', 13], ['homeothermic', 14],
    ['homeothermic', 15], ['homeothermic', 16], ['has_eggs', 2], ['has_eggs', 4],
    ['has_eggs', 5], ['has_eggs', 6], ['has_eggs', 7], ['has_eggs', 8], ['has_eggs', 9],
    ['has_eggs', 10], ['has_eggs', 11], ['has_eggs', 12], ['has_eggs', 13],
    ['has_eggs', 14], ['has_eggs', 15], ['has_gills', 4], ['has_gills', 5],
    ['has_gills', 6], ['has_gills', 7]
]
output_tuples = [
    ['mammal', 0], ['mammal',1], ['mammal', 2], ['mammal', 3],
    ['fish', 4], ['fish', 5], ['fish', 6], ['fish', 7],
    ['reptile', 8], ['reptile', 9], ['reptile', 10], ['reptile', 11], ['reptile', 12],
    ['bird', 13], ['bird', 14], ['bird', 15]
]

true_rules = [
['bird(x0:A)','feathers(x1:C)','has_covering(x0:A,x1:C)'],
['fish(x0:A)','has_gills(x0:A)'],
['mammal(x0:A)','has_covering(x0:A,x1:C)','has_milk(x0:A)'],
['reptile(x0:A)','has_covering(x0:A,x1:C)','scales(x1:C)'],
]
    
rules = [
['bird(x0:A)','reptile(x0:A)'],
['bird(x0:A)','mammal(x0:A)'],
['bird(x0:A)','fish(x0:A)'],
['bird(x0:A)','homeothermic(x0:A)'],
['bird(x0:A)','has_eggs(x0:A)'],
['bird(x0:A)','has_milk(x0:A)'],
['bird(x0:A)','has_gills(x0:A)'],
['bird(x0:A)','has_covering(x0:A,x1:C)'],
['bird(x0:A)','has_covering(x0:A,x1:C)','reptile(x0:A)'],
['bird(x0:A)','has_covering(x0:A,x1:C)','mammal(x0:A)'],
['bird(x0:A)','fish(x0:A)','has_covering(x0:A,x1:C)'],
['bird(x0:A)','has_covering(x0:A,x1:C)','homeothermic(x0:A)'],
['bird(x0:A)','has_covering(x0:A,x1:C)','has_eggs(x0:A)'],
['bird(x0:A)','has_covering(x0:A,x1:C)','has_milk(x0:A)'],
['bird(x0:A)','has_covering(x0:A,x1:C)','has_gills(x0:A)'],
['bird(x0:A)','feathers(x1:C)','has_covering(x0:A,x1:C)'],
['bird(x0:A)','has_covering(x0:A,x1:C)','scales(x1:C)'],
['bird(x0:A)','hair(x1:C)','has_covering(x0:A,x1:C)'],
['bird(x0:A)','has_covering(x0:A,x1:C)','none(x1:C)'],
['fish(x0:A)','reptile(x0:A)'],
['fish(x0:A)','mammal(x0:A)'],
['fish(x0:A)','bird(x0:A)'],
['fish(x0:A)','homeothermic(x0:A)'],
['fish(x0:A)','has_eggs(x0:A)'],
['fish(x0:A)','has_milk(x0:A)'],
['fish(x0:A)','has_gills(x0:A)'],
['fish(x0:A)','has_covering(x0:A,x1:C)'],
['fish(x0:A)','has_covering(x0:A,x1:C)','reptile(x0:A)'],
['fish(x0:A)','has_covering(x0:A,x1:C)','mammal(x0:A)'],
['fish(x0:A)','bird(x0:A)','has_covering(x0:A,x1:C)'],
['fish(x0:A)','has_covering(x0:A,x1:C)','homeothermic(x0:A)'],
['fish(x0:A)','has_covering(x0:A,x1:C)','has_eggs(x0:A)'],
['fish(x0:A)','has_covering(x0:A,x1:C)','has_milk(x0:A)'],
['fish(x0:A)','has_covering(x0:A,x1:C)','has_gills(x0:A)'],
['fish(x0:A)','feathers(x1:C)','has_covering(x0:A,x1:C)'],
['fish(x0:A)','has_covering(x0:A,x1:C)','scales(x1:C)'],
['fish(x0:A)','hair(x1:C)','has_covering(x0:A,x1:C)'],
['fish(x0:A)','has_covering(x0:A,x1:C)','none(x1:C)'],
['mammal(x0:A)','reptile(x0:A)'],
['mammal(x0:A)','fish(x0:A)'],
['mammal(x0:A)','bird(x0:A)'],
['mammal(x0:A)','homeothermic(x0:A)'],
['mammal(x0:A)','has_eggs(x0:A)'],
['mammal(x0:A)','has_milk(x0:A)'],
['mammal(x0:A)','has_gills(x0:A)'],
['mammal(x0:A)','has_covering(x0:A,x1:C)'],
['mammal(x0:A)','has_covering(x0:A,x1:C)','reptile(x0:A)'],
['mammal(x0:A)','fish(x0:A)','has_covering(x0:A,x1:C)'],
['mammal(x0:A)','bird(x0:A)','has_covering(x0:A,x1:C)'],
['mammal(x0:A)','has_covering(x0:A,x1:C)','homeothermic(x0:A)'],
['mammal(x0:A)','has_covering(x0:A,x1:C)','has_eggs(x0:A)'],
['mammal(x0:A)','has_covering(x0:A,x1:C)','has_milk(x0:A)'],
['mammal(x0:A)','has_covering(x0:A,x1:C)','has_gills(x0:A)'],
['mammal(x0:A)','feathers(x1:C)','has_covering(x0:A,x1:C)'],
['mammal(x0:A)','has_covering(x0:A,x1:C)','scales(x1:C)'],
['mammal(x0:A)','hair(x1:C)','has_covering(x0:A,x1:C)'],
['mammal(x0:A)','has_covering(x0:A,x1:C)','none(x1:C)'],
['reptile(x0:A)','mammal(x0:A)'],
['reptile(x0:A)','fish(x0:A)'],
['reptile(x0:A)','bird(x0:A)'],
['reptile(x0:A)','homeothermic(x0:A)'],
['reptile(x0:A)','has_eggs(x0:A)'],
['reptile(x0:A)','has_milk(x0:A)'],
['reptile(x0:A)','has_gills(x0:A)'],
['reptile(x0:A)','has_covering(x0:A,x1:C)'],
['reptile(x0:A)','has_covering(x0:A,x1:C)','mammal(x0:A)'],
['reptile(x0:A)','fish(x0:A)','has_covering(x0:A,x1:C)'],
['reptile(x0:A)','bird(x0:A)','has_covering(x0:A,x1:C)'],
['reptile(x0:A)','has_covering(x0:A,x1:C)','homeothermic(x0:A)'],
['reptile(x0:A)','has_covering(x0:A,x1:C)','has_eggs(x0:A)'],
['reptile(x0:A)','has_covering(x0:A,x1:C)','has_milk(x0:A)'],
['reptile(x0:A)','has_covering(x0:A,x1:C)','has_gills(x0:A)'],
['reptile(x0:A)','feathers(x1:C)','has_covering(x0:A,x1:C)'],
['reptile(x0:A)','has_covering(x0:A,x1:C)','scales(x1:C)'],
['reptile(x0:A)','hair(x1:C)','has_covering(x0:A,x1:C)'],
['reptile(x0:A)','has_covering(x0:A,x1:C)','none(x1:C)'],
]

rule_weights = {
    '991':
    [(0,0.01), (1,0.01), (2,0.01), (3,0.01), (4,0.01), (5,0.01), (6,0.01), (7,0.01), (8,0.01), (9,0.01), (10,0.01), (11,0.01), (12,0.01), (13,0.01), (14,0.01), (15,0.99), (16,0.01), (17,0.01), (18,0.01), (19,0.01), (20,0.01), (21,0.01), (22,0.01), (23,0.01), (24,0.01), (25,0.99), (26,0.01), (27,0.01), (28,0.01), (29,0.01), (30,0.01), (31,0.01), (32,0.01), (33,0.21993073277985753), (34,0.01), (35,0.01), (36,0.01), (37,0.01), (38,0.01), (39,0.01), (40,0.01), (41,0.01), (42,0.01), (43,0.01), (44,0.01), (45,0.01), (46,0.01), (47,0.01), (48,0.01), (49,0.01), (50,0.01), (51,0.99), (52,0.01), (53,0.01), (54,0.01), (55,0.619097549391895), (56,0.01), (57,0.01), (58,0.0022163966978497873), (59,0.01), (60,0.01), (61,0.01), (62,0.01), (63,0.01), (64,0.01), (65,0.01), (66,0.01), (67,0.004937857275491231), (68,0.01), (69,0.01), (70,0.01), (71,0.0043282735104289705), (72,0.01), (73,0.99), (74,0.01), (75,0.01)],
}

base = 4
chain = None
nc = 4
nl = 2
bound = 20

