input_domains = {'C' : 5, 'V' : 12, 'H' : 12, 'M' : 3, 'F' : 3, 'Z' : 3}

# input: [name, arity, dimension0, dimension1, ...]
input_relations = {'points_initial': ['V', 'H'], 'store': ['V', 'F', 'V'],
                   'load': ['V', 'F', 'V'], 'invocation': ['C', 'C', 'H', 'C', 'C', 'M'],
                   'actual': ['H', 'Z', 'V'], 'formal': ['M', 'Z', 'V'],
                   'assign': ['C', 'C', 'V', 'C', 'C', 'V']}
input_tuples = [['points_initial', 1, 1], ['points_initial', 2, 2], ['points_initial', 5, 1], ['points_initial', 9, 9], ['points_initial', 11, 11], ['store', 7, 2, 5], ['store', 5, 1, 1], ['store', 9, 2, 5], ['store', 9, 2, 2], ['load', 2, 2, 8], ['load', 5, 1, 10], ['load', 5, 1, 7], ['invocation', 1, 1, 1, 2, 3, 1], ['invocation', 3, 1, 2, 2, 3, 1], ['invocation', 2, 3, 9, 1, 1, 1], ['actual', 1, 0, 5], ['actual', 1, 1, 7], ['actual', 2, 0, 6], ['actual', 2, 1, 2], ['formal', 1, 0, 5], ['formal', 1, 1, 7], ['formal', 2, 0, 3], ['formal', 2, 1, 6], ['assign', 2, 3, 5, 1, 1, 5], ['assign', 2, 3, 7, 1, 1, 7], ['assign', 2, 3, 5, 3, 1, 6], ['assign', 2, 3, 7, 3, 1, 2], ['assign', 2, 3, 8, 3, 4, 2], ['assign', 2, 3, 8, 2, 4, 2], ['assign', 2, 3, 8, 2, 1, 2]]

# output
output_relations = {'pointsto': ['C', 'C', 'V', 'H'], 'heappointsto': ['H', 'F', 'H']}
output_tuples = [['pointsto', 1, 1, 1, 1], ['pointsto', 1, 1, 5, 1], ['pointsto', 3, 1, 2, 2], ['pointsto', 2, 3, 9, 9], ['pointsto', 2, 3, 5, 1], ['pointsto', 2, 3, 7, 2], ['pointsto', 1, 1, 10, 1], ['pointsto', 1, 1, 7, 1], ['pointsto', 2, 3, 7, 1], ['pointsto', 3, 1, 8, 1], ['pointsto', 2, 3, 10, 1], ['heappointsto', 1, 1, 1], ['heappointsto', 2, 2, 1], ['heappointsto', 1, 2, 1], ['heappointsto', 9, 2, 1]]

# rules
new_rules = [
['pointsto(x2:C,x4:C,x0:V,x1:H)','invocation(x2:C,x4:C,x1:H,x3:C,x5:C,x4:M)','points_initial(x0:V,x1:H)'],
['pointsto(x2:C,x5:C,x3:V,x1:H)','assign(x2:C,x5:C,x3:V,x4:C,x6:C,x0:V)','pointsto(x4:C,x6:C,x0:V,x1:H)'],
['pointsto(x0:C,x6:C,x1:V,x2:H)','heappointsto(x5:H,x4:F,x2:H)','load(x3:V,x4:F,x1:V)','pointsto(x0:C,x6:C,x3:V,x5:H)'],
['heappointsto(x0:H,x1:F,x2:H)','pointsto(x5:C,x6:C,x3:V,x0:H)','pointsto(x5:C,x6:C,x4:V,x2:H)','store(x3:V,x1:F,x4:V)']
]
rules = [['pointsto(x2:C,x3:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x2:C,x4:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x2:C,x5:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x3:C,x2:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x3:C,x4:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x3:C,x5:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x4:C,x2:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x4:C,x3:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x5:C,x2:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x5:C,x3:C,x0:V,x1:H)', 'invocation(x2:C,x3:C,x1:H,x4:C,x5:C,x6:M)', 'points_initial(x0:V,x1:H)'], ['pointsto(x2:C,x3:C,x0:V,x1:H)', 'assign(x2:C,x3:C,x0:V,x4:C,x5:C,x6:V)', 'points_initial(x0:V,x1:H)'], ['pointsto(x2:C,x3:C,x0:V,x1:H)', 'assign(x2:C,x3:C,x4:V,x5:C,x6:C,x0:V)', 'points_initial(x0:V,x1:H)'], ['pointsto(x2:C,x3:C,x4:V,x1:H)', 'assign(x2:C,x3:C,x4:V,x5:C,x6:C,x0:V)', 'points_initial(x0:V,x1:H)'], ['pointsto(x2:C,x5:C,x4:V,x1:H)', 'assign(x2:C,x3:C,x4:V,x5:C,x6:C,x0:V)', 'points_initial(x0:V,x1:H)'], ['pointsto(x2:C,x6:C,x4:V,x1:H)', 'assign(x2:C,x3:C,x4:V,x5:C,x6:C,x0:V)', 'points_initial(x0:V,x1:H)'], ['pointsto(x5:C,x3:C,x4:V,x1:H)', 'assign(x2:C,x3:C,x4:V,x5:C,x6:C,x0:V)', 'points_initial(x0:V,x1:H)'], ['pointsto(x6:C,x3:C,x4:V,x1:H)', 'assign(x2:C,x3:C,x4:V,x5:C,x6:C,x0:V)', 'points_initial(x0:V,x1:H)'], ['pointsto(x2:C,x3:C,x0:V,x1:H)', 'points_initial(x0:V,x1:H)', 'pointsto(x2:C,x3:C,x0:V,x4:H)'], ['pointsto(x3:C,x2:C,x0:V,x1:H)', 'points_initial(x0:V,x1:H)', 'pointsto(x2:C,x3:C,x0:V,x4:H)'], ['pointsto(x3:C,x2:C,x0:V,x4:H)', 'points_initial(x0:V,x1:H)', 'pointsto(x2:C,x3:C,x0:V,x4:H)'], ['pointsto(x2:C,x3:C,x0:V,x1:H)', 'points_initial(x0:V,x1:H)', 'pointsto(x2:C,x3:C,x4:V,x1:H)'], ['pointsto(x3:C,x2:C,x0:V,x1:H)', 'points_initial(x0:V,x1:H)', 'pointsto(x2:C,x3:C,x4:V,x1:H)'], ['pointsto(x3:C,x2:C,x4:V,x1:H)', 'points_initial(x0:V,x1:H)', 'pointsto(x2:C,x3:C,x4:V,x1:H)'], ['pointsto(x3:C,x4:C,x5:V,x0:H)', 'actual(x0:H,x1:Z,x2:V)', 'assign(x3:C,x4:C,x5:V,x6:C,x7:C,x2:V)'], ['pointsto(x3:C,x4:C,x2:V,x0:H)', 'actual(x0:H,x1:Z,x2:V)', 'pointsto(x3:C,x4:C,x5:V,x0:H)'], ['pointsto(x3:C,x4:C,x2:V,x0:H)', 'actual(x0:H,x1:Z,x2:V)', 'pointsto(x3:C,x4:C,x2:V,x5:H)'], ['pointsto(x3:C,x4:C,x2:V,x5:H)', 'pointsto(x3:C,x4:C,x0:V,x5:H)', 'store(x0:V,x1:F,x2:V)'], ['pointsto(x3:C,x4:C,x2:V,x5:H)', 'load(x0:V,x1:F,x2:V)', 'pointsto(x3:C,x4:C,x0:V,x5:H)'], ['pointsto(x4:C,x3:C,x0:V,x5:H)', 'pointsto(x3:C,x4:C,x0:V,x5:H)', 'store(x0:V,x1:F,x2:V)'], ['pointsto(x4:C,x3:C,x0:V,x5:H)', 'load(x0:V,x1:F,x2:V)', 'pointsto(x3:C,x4:C,x0:V,x5:H)'], ['pointsto(x0:C,x1:C,x7:V,x8:H)', 'invocation(x0:C,x1:C,x2:H,x3:C,x4:C,x5:M)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x7:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x7:V,x8:H)', 'invocation(x0:C,x1:C,x2:H,x3:C,x4:C,x5:M)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x7:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x0:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x0:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x1:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x1:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x2:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x5:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x3:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x4:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x6:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x3:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x4:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x6:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x3:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x3:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x4:C,x6:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x5:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x0:C,x3:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x0:C,x4:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x0:C,x6:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x3:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x4:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x6:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x4:C,x7:V,x8:H)'], ['pointsto(x0:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x0:C,x1:C,x5:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x0:C,x3:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x0:C,x4:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x0:C,x6:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x0:C,x7:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x3:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x4:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x6:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x7:C,x1:C,x2:V,x8:H)', 'assign(x0:C,x1:C,x2:V,x3:C,x4:C,x5:V)', 'pointsto(x6:C,x7:C,x5:V,x8:H)'], ['pointsto(x3:C,x4:C,x5:V,x2:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'pointsto(x3:C,x4:C,x5:V,x0:H)'], ['pointsto(x4:C,x3:C,x5:V,x2:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'pointsto(x3:C,x4:C,x5:V,x0:H)'], ['pointsto(x0:C,x1:C,x2:V,x6:H)', 'pointsto(x0:C,x1:C,x2:V,x3:H)', 'pointsto(x0:C,x4:C,x5:V,x6:H)'], ['pointsto(x0:C,x1:C,x2:V,x6:H)', 'pointsto(x0:C,x1:C,x2:V,x3:H)', 'pointsto(x4:C,x0:C,x5:V,x6:H)'], ['pointsto(x4:C,x0:C,x5:V,x3:H)', 'pointsto(x0:C,x1:C,x2:V,x3:H)', 'pointsto(x4:C,x0:C,x5:V,x6:H)'], ['pointsto(x0:C,x1:C,x2:V,x6:H)', 'pointsto(x0:C,x1:C,x2:V,x3:H)', 'pointsto(x4:C,x1:C,x5:V,x6:H)'], ['pointsto(x0:C,x1:C,x2:V,x6:H)', 'pointsto(x0:C,x1:C,x2:V,x3:H)', 'pointsto(x4:C,x5:C,x2:V,x6:H)'], ['pointsto(x0:C,x1:C,x2:V,x3:H)', 'assign(x0:C,x1:C,x2:V,x4:C,x5:C,x6:V)', 'pointsto(x4:C,x5:C,x6:V,x3:H)'], ['pointsto(x0:C,x1:C,x2:V,x3:H)', 'heappointsto(x6:H,x5:F,x3:H)', 'pointsto(x0:C,x1:C,x4:V,x6:H)', 'store(x4:V,x5:F,x2:V)'], ['pointsto(x0:C,x1:C,x2:V,x3:H)', 'heappointsto(x6:H,x5:F,x3:H)', 'load(x4:V,x5:F,x2:V)', 'pointsto(x0:C,x1:C,x4:V,x6:H)'], ['heappointsto(x3:H,x2:F,x1:H)', 'heappointsto(x1:H,x2:F,x3:H)', 'points_initial(x0:V,x1:H)'], ['heappointsto(x4:H,x3:F,x0:H)', 'actual(x0:H,x1:Z,x2:V)', 'heappointsto(x0:H,x3:F,x4:H)'], ['heappointsto(x0:H,x4:F,x3:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x0:H,x4:F,x3:H)', 'actual(x0:H,x1:Z,x2:V)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x0:H,x1:F,x4:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x0:H,x3:F,x4:H)'], ['heappointsto(x2:H,x1:F,x4:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x0:H,x3:F,x4:H)'], ['heappointsto(x2:H,x3:F,x4:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x0:H,x3:F,x4:H)'], ['heappointsto(x0:H,x1:F,x3:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x0:H,x4:F,x2:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x2:H,x1:F,x0:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x2:H,x1:F,x3:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x2:H,x4:F,x0:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x2:H,x4:F,x3:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x3:H,x1:F,x0:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x3:H,x1:F,x2:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x3:H,x4:F,x2:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x0:H)'], ['heappointsto(x0:H,x1:F,x3:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x1:F,x4:H)'], ['heappointsto(x0:H,x1:F,x4:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x1:F,x4:H)'], ['heappointsto(x2:H,x1:F,x3:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x1:F,x4:H)'], ['heappointsto(x2:H,x1:F,x4:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x1:F,x4:H)'], ['heappointsto(x0:H,x1:F,x3:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x2:H)'], ['heappointsto(x0:H,x4:F,x2:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x2:H)'], ['heappointsto(x0:H,x4:F,x3:H)', 'heappointsto(x0:H,x1:F,x2:H)', 'heappointsto(x3:H,x4:F,x2:H)'], ['heappointsto(x0:H,x1:F,x2:H)', 'pointsto(x5:C,x6:C,x3:V,x0:H)', 'pointsto(x5:C,x6:C,x4:V,x2:H)', 'store(x3:V,x1:F,x4:V)'], ['heappointsto(x0:H,x1:F,x2:H)', 'load(x3:V,x1:F,x4:V)', 'pointsto(x5:C,x6:C,x3:V,x0:H)', 'pointsto(x5:C,x6:C,x4:V,x2:H)']]

# for ZAATAR
base = 1
chain = None
nc = 6
nl = 2
bound = 20