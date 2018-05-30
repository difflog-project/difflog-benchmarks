input_domains = {'P' : 120 }
input_relations = {'nausea': ['P'], 'not_nausea': ['P'], 'lumbar_pain': ['P'],
                   'not_lumbar_pain': ['P'], 'urine_pushing': ['P'],
                   'not_urine_pushing': ['P'], 'micturition_pain': ['P'],
                   'not_micturition_pain': ['P'], 'burning_urethra': ['P'],
                   'not_burning_urethra': ['P']}
output_relations = {'inflammation': ['P']}

nausea = [70,71,72,75,76,78,79,81,83,84,85,88,89,91,92,98,99,101,105,106,108,110,114]
lumbar_pain = [0,2,5,7,11,14,15,19,22,32,34,37,40,41,50,52,57,60,62,63,64,65,66,67,
        68,69,70,71,72,75,76,77,78,79,81,82,83,84,85,88,89,91,92,97,98,99,100,101,
        104,105,106,108,109,110,113,114,115,118]
not_urine_pushing = [0,2,5,7,11,14,15,19,22,32,34,37,40,41,50,52,57,73,74,75,76,80,
        81,86,90,91,94,102,107,108,111,116]
micturition_pain = [1,3,6,8,9,10,17,18,20,21,23,24,25,26,29,31,35,39,42,46,48,53,55,
        58,70,71,72,75,76,78,79,81,83,84,85,88,89,91,92,98,99,101,105,106,108,110,114]
burning_urethra = [1,3,6,8,9,10,17,18,23,24,25,26,29,35,42,53,58,60,62,63,64,65,66,
        67,68,69,70,71,77,79,82,83,89,92,97,100,101,104,105,109,110,113,115,118,119]
inflammation = [1,3,6,8,9,10,17,18,20,21,23,24,25,26,27,29,30,31,35,36,38,39,42,
        43,44,46,48,53,55,58,59,70,71,72,78,79,83,84,85,88,89,92,98,99,101,105,
        106,110,114]

input_tuples = []
output_tuples = []

# definitions sould be contiguous for Metagol
for i in range(120):
    if i in nausea:
        input_tuples.append(['nausea', i])

for i in range(120):
    if i not in nausea:
        input_tuples.append(['not_nausea', i])

for i in range(120):
    if i in lumbar_pain:
        input_tuples.append(['lumbar_pain', i])

for i in range(120):
    if i not in lumbar_pain:
        input_tuples.append(['not_lumbar_pain', i])

for i in range(120):
    if i in not_urine_pushing:
        input_tuples.append(['not_urine_pushing', i])

for i in range(120):
    if i not in  not_urine_pushing:
        input_tuples.append(['urine_pushing', i])

for i in range(120):
    if i in micturition_pain:
        input_tuples.append(['micturition_pain', i])

for i in range(120):
    if i not in micturition_pain:
        input_tuples.append(['not_micturition_pain', i])

for i in range(120):
    if i in burning_urethra:
        input_tuples.append(['burning_urethra', i])

for i in range(120):
    if i not in burning_urethra:
        input_tuples.append(['not_burning_urethra', i])

for i in range(120):
    if i in inflammation:
        output_tuples.append(['inflammation', i])

rules = [
['inflamation(x0:P)','lumbar_pain(x0:P)','not_burning_urethra(x0:P)'],
['inflamation(x0:P)','lumbar_pain(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','lumbar_pain(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','lumbar_pain(x0:P)','micturition_pain(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','lumbar_pain(x0:P)'],
['inflamation(x0:P)','lumbar_pain(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','lumbar_pain(x0:P)','not_lumbar_pain(x0:P)'],
['inflamation(x0:P)','lumbar_pain(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','lumbar_pain(x0:P)','nausea(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_burning_urethra(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_burning_urethra(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','not_lumbar_pain(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_burning_urethra(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','not_micturition_pain(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','not_micturition_pain(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','not_lumbar_pain(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','not_micturition_pain(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','not_micturition_pain(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','not_nausea(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','not_lumbar_pain(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','not_urine_pushing(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_burning_urethra(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','micturition_pain(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_lumbar_pain(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','nausea(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_burning_urethra(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','micturition_pain(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_lumbar_pain(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','nausea(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','not_micturition_pain(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','not_nausea(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','not_lumbar_pain(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','not_nausea(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','not_lumbar_pain(x0:P)'],
['inflamation(x0:P)','not_lumbar_pain(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','not_lumbar_pain(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_lumbar_pain(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_lumbar_pain(x0:P)'],
['inflamation(x0:P)','not_lumbar_pain(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','not_lumbar_pain(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_lumbar_pain(x0:P)'],
['inflamation(x0:P)','not_burning_urethra(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','not_micturition_pain(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','not_urine_pushing(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','not_nausea(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','not_lumbar_pain(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_urine_pushing(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_burning_urethra(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_micturition_pain(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','micturition_pain(x0:P)','nausea(x0:P)'],
['inflamation(x0:P)','burning_urethra(x0:P)','nausea(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_nausea(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_lumbar_pain(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','not_urine_pushing(x0:P)'],
]

true_rules = [
['inflamation(x0:P)','not_lumbar_pain(x0:P)','urine_pushing(x0:P)'],
['inflamation(x0:P)','nausea(x0:P)','urine_pushing(x0:P)'],
]

base = 1
chain = None
nc = 1
nl = 3
bound = 20

