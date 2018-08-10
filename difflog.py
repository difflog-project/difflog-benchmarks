from rule import Rule
from predicate import Predicate
import relation

import copy
import itertools
import math
import random
import sys
import time

#from frozendict import frozendict
import numpy as np

def product(args):
    p = 1
    for arg in args:
        p *= arg
    return p

def product_provenance(args):
    p = 1
    for arg in args:
        p *= arg[1]
    return p

def gradient_length(m):
    total = 0
    for x in m:
        total += m[x] * m[x]
    return total

def vars_of_pred(p):
    return set(p.doms)

def vars_of_rule(r):
    x = set()
    for p in r.body_preds:
        x = x.union(vars_of_pred(p))
    return x

def get_domains(num_domains, domain_size):
    to_return = []
    for i in range(num_domains):
        to_return.append(list(range(domain_size)))
    return to_return

def indices_of(arr):
    to_return = []
    for i in arr.shape:
        to_return.append(list(range(i)))
    return itertools.product(*to_return)

def restrict(x):
    return min(max(x, 0), 1)

def generate_map(r, l):
    out = []
    for x in l:
        generated = {}
        for i in range(len(x)):
            generated[r.doms[i]] = x[i]
        
        out.append(generated)
    
    return out

def map_input(l):
    result = {}
    for x in l:
        result[x] = 1
    return result
    
class DiffLog(object):
    def __init__(self):
        self.time = 0
        self.valuation = {} # Map from relation names to list of tuples in relation
        self.relation_map = {} # Map from relation names to np arrays of ints
        self.correct_relations = {} # Correct values
        self.outputs = [] # List of "output relations"
        self.rules = [] # Map of rules to numbers
        self.inputs = []

        self.last_added = {}
        self.current_added = {}

        self.changed = False
        self.domain_size = 0 # size of domain
        self.provenance = {} # Map from relation names to np arrays of rules

    def parse_rules_max(self, s):
        for l in s:
            self.rules.append((Rule(l), 1))

    def parse_rules(self, s):
        for l in s:
            self.rules.append((Rule(l), random.random()))

    def add_result_domain(self, name, dims, facts):
        self.valuation[name] = {}
        self.last_added[name] = {}
        self.current_added[name] = {}
        self.relation_map[name] = np.zeros((dims))
        self.domain_size = dims[0]
        self.provenance[name] = {}
    
        output_domain = np.zeros((dims))
        relation.fill_map(output_domain, facts)
        self.correct_relations[name] = output_domain

        self.outputs.append(name)

    def add_anon_domain(self, name, dims):
        self.valuation[name] = {}
        self.last_added[name] = {}
        self.current_added[name] = {}
        self.relation_map[name] = np.zeros((dims))
        self.provenance[name] = {}
        self.outputs.append(name)

    def add_input_domain(self, name, dims, facts):
        input_domain = np.zeros((dims))
        relation.fill_map(input_domain, facts)
        self.relation_map[name] = input_domain
        self.valuation[name] = map_input(facts)
        self.last_added[name] = map_input(facts)
        self.current_added[name] = {}
        self.provenance[name] = {}
        self.inputs.append(name)

    def filter_rules(self, n):
        new_rules = []
        for r in self.rules:
            vs = set()
            for v in r[0].body_preds:
                for d in v.doms:
                    vs.add(d)
            if len(vs) <= n:
                new_rules.append(r)
        self.rules = new_rules

    def hash_merge(self, m1, m2, m1_doms, m2_doms):
        if len(m1) == 0:
            return m1
        if len(m2) == 0:
            return m2

        shared_doms = []
        for x in m1_doms:
            if x in m2_doms:
                shared_doms.append(x)

        larger = m1
        smaller = m2
        if len(m1) < len(m2):
            larger, smaller = smaller, larger

        hash_map = {}
        for (smaller_map, smaller_weight, smaller_provenance) in smaller:
            t = []
            for v in shared_doms:
                t.append(smaller_map[v])
            
            if tuple(t) not in hash_map:
                hash_map[tuple(t)] = []
            hash_map[tuple(t)].append((smaller_map, smaller_weight, smaller_provenance))
        out_map = []
        for (larger_map, larger_weight, larger_provenance) in larger:
            t = []
            for v in shared_doms:
                t.append(larger_map[v])

            if tuple(t) in hash_map:
                join_with = hash_map[tuple(t)]
                for (join_with_map, join_with_weight, join_with_provenance) in join_with:
                    combined = {}
                    for (v, w) in join_with_map.items():
                        combined[v] = w
                    for (v, w) in larger_map.items():
                        combined[v] = w

                    new_weight = join_with_weight * larger_weight
                    # may have duplications but ignore for performance
                    out_map.append((combined, new_weight, join_with_provenance + larger_provenance))
        return out_map

    def iter_merge(self, m1, m2):
        new_mappings = {}
        for v1 in m1:
            for v2 in m2:
                compatible = True
                for x in v1:
                    if x in v2 and v1[x] != v2[x]:
                        compatible = False
                        break
                    
                if compatible:
                    combined = {}
                    for x in v1:
                        combined[x] = v1[x]
                    for x in v2:
                        combined[x] = v2[x]

                    combined = frozendict(combined)
                    new_weight = m1[v1][0] * m2[v2][0]
                    if combined not in new_mappings or new_mappings[combined] < new_weight:
                        new_mappings[combined] = (new_weight, m1[v1][1] + m2[v2][1])
    
        return new_mappings

    def join(self, r, r_index, index, points):
        incr = 0
        assignment = {}
        for v in vars_of_rule(r[0]):
            assignment[v] = incr
            incr += 1

        i = 1
        var_mappings = self.generate_map(r[0].body_preds[0], index == 0)
        for b in r[0].body_preds[1:]:
            if len(var_mappings) == 0:
                break

            doms = []
            for x in var_mappings:
                for v in x[0]:
                    doms.append(v)
                break

            v2_map = self.generate_map(b, index == i)

            var_mappings = self.hash_merge(var_mappings, v2_map, doms, b.doms)
            i += 1

        for (x, weight, provenance) in var_mappings:
            coords = []
            for v in r[0].head_pred.doms:
                if v not in x:
                    print r[0].head_pred.doms
                    print x
                coords.append(x[v])

            if tuple(coords) not in points or points[tuple(coords)][0] < weight * r[1]:
                points[tuple(coords)] = (weight * r[1], provenance + [(r_index, r[1])])
        return points

    def eval_rule(self, r, r_index):
        if r[1] == 0:
            return 

        incr = 0
        assignment = {}
        for v in vars_of_rule(r[0]):
            assignment[v] = incr
            incr += 1

        points = {}
        for i in range(len(r[0].body_preds)):
            points = self.join(r, r_index, i, points)

        name = r[0].head_pred.name
        for x in points:
            if x not in self.valuation[name] or self.valuation[name][x] < points[x][0]:
                self.changed = True
                self.valuation[name][x] = points[x][0]
                self.relation_map[name][x] = points[x][0]
                self.provenance[name][x] = points[x][1]
                self.current_added[name][x] = points[x][0]
        
    def eval_rules(self):
        for i in range(len(self.rules)):
            self.eval_rule(self.rules[i], i)

    def eval_rule_initial(self, r, r_index):
        """
        This function exists because on the first run of semi-naive evaluation
        we do not need to do the difference trick.
        """
        if r[1] == 0:
            return

        incr = 0
        assignment = {}
        for v in vars_of_rule(r[0]):
            assignment[v] = incr
            incr += 1

        # hack, but basically indicates we should do the full join
        points = self.join(r, r_index, -1, {})

        name = r[0].head_pred.name
        for x in points:
            if x not in self.valuation[name] or self.valuation[name][x] < points[x][0]:
                self.changed = True
                self.valuation[name][x] = points[x][0]
                self.relation_map[name][x] = points[x][0]
                self.provenance[name][x] = points[x][1]
                self.current_added[name][x] = points[x][0]

    def eval_rules_initial(self):
        for i in range(len(self.rules)):
            self.eval_rule_initial(self.rules[i], i)

    def relations_equal(self, rs):
        for r in rs:
            if not (rs[r] == self.relation_map[r]).all():
                return False
        return True
    
    def eval_program(self):
        t = time.clock()
        self.eval_rules_initial()
        iters = 0
        while self.changed:
            iters += 1
            #if self.relations_equal(original):
            #    break
            #if not self.changed:
            #    break
            self.changed = False

            # Reinitialize seminaive relations
            self.last_added = self.current_added
            self.current_added = {}
            for x in self.last_added:
                self.current_added[x] = {}

            self.eval_rules()
        
        self.time += time.clock() - t

    def adjust_weights(self):
        adjustments = {}
        for r in self.correct_relations:
            for p in indices_of(self.correct_relations[r]):
                if p not in self.provenance[r]:
                    continue

                product = product_provenance(self.provenance[r][p])
                if product == 0:
                    print self.correct_relations[r][p]
                    print self.relation_map[r][p]
                    print self.provenance[r][p]
                    exit()
                    continue

                for t in self.provenance[r][p]:
                    if t[0] not in adjustments:
                        adjustments[t[0]] = 0
                   
                    adjustments[t[0]] += product / t[1] * (self.correct_relations[r][p] - self.relation_map[r][p])
                    #if self.correct_relations[r][p] > self.relations[r][p]:
                    #    adjustments[t[0]] += product / t[1]
                    #else:
                    #    adjustments[t[0]] -= product / t[1]
        
        if gradient_length(adjustments) == 0:
            return False

        alpha = self.calc_error() / gradient_length(adjustments)

        for k in adjustments:
            k = int(k)
            # Think about this
            self.rules[k] = (self.rules[k][0], restrict(self.rules[k][1] + adjustments[k] * alpha))

        return True

    def calc_error(self):
        error = 0
        for r in self.correct_relations:
            for p in indices_of(self.correct_relations[r]):
                delta = self.correct_relations[r][p] - self.relation_map[r][p]
                error += delta * delta
                #error += abs(self.correct_relations[r][p] - self.relations[r][p])
        
        return error

    def get_program(self):
        num_iters = 0
        while num_iters < 100:
            if num_iters > 0:
                if not self.adjust_weights():
                    print "here"
                    break

                #for r in self.rules:
                #    print r

            for out in self.outputs:
                self.relation_map[out] = np.zeros(self.relation_map[out].shape)
                self.valuation[out] = {}
                self.last_added[out] = {} # Inputs shouldn't have changed?
                self.provenance[out] = {}

            for i in self.inputs:
                self.last_added[i] = self.valuation[i]
            self.eval_program()
            
            error = self.calc_error()
            print "iteration {}: {}".format(num_iters, error)
            if error < 0.05:
                break
            
            sys.stdout.flush()
            num_iters += 1

        print num_iters

    def generate_map(self, r, is_old=False):
        if is_old:
            l = self.last_added[r.name]
        else:
            l = self.valuation[r.name]
        
        out = []
        for x in l:
            generated = {}
            for i in range(len(x)):
                generated[r.doms[i]] = x[i]

            if x not in self.provenance[r.name]:
                self.provenance[r.name][x] = []
            out.append((generated, l[x], self.provenance[r.name][x]))

        return out

if __name__ == "__main__":
    random.seed(1000)
    d = DiffLog()
    d.add_result_domain("path", (5, 5), [(0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1,3), (1, 4), (2, 3), (2, 4), (3, 4)])
    d.add_input_domain("edge", (5, 5), [(0, 1), (1,2), (2, 3), (3, 4)])
    d.parse_rules(["path(x,y) :- edge(x,y).", "path(x,y) :- edge(x, z), path(z, y)."])
    #d.parse_rules(["path(x,y) :- edge(y,x)."])

    for r in d.rules:
        print r
    #d.get_program()
    #print d.rules
    #print d.relations
    #print d.rules
    #print d.domain_size

    d.eval_rules()
    #d.eval_program()
    #print d.valuation['path']
    print d.relation_map['path']
    print d.correct_relations
    #for x in d.provenance['path']:
    #    print (x, d.provenance['path'][x])
    
    #print d.generate_map(Predicate("edge(x,y)."))

