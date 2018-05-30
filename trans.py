#!/usr/bin/env python2
# usage example: ./trans.py -t zaatar benchmark/andersen.py

import argparse
import importlib

import make_random

parser = argparse.ArgumentParser(description='Translator')
parser.add_argument("file", help="Filename")
parser.add_argument("-t", "--to", required=True, help="Target Format")
parser.add_argument("-r", "--random", help="Introduce noise", default=0.0, type=float)
parser.add_argument("--weight", help="Assign learned weight rather than 0.5", type=str)
args = parser.parse_args()

module_name = args.file.replace("/", ".").replace(".py", "")
benchmark = importlib.import_module(module_name)

original_output = benchmark.output_tuples
if args.random > 0.0:
    make_random.inject_noise(benchmark, args.random)

if args.to == "zaatar":
    max_size = 0
    for (d, size) in benchmark.input_domains.items():
        max_size += size

    print("=" * 100)
    print("Copy the following lines")
    print("=" * 100)
    print("elif args.benchmark == \"" + module_name.split('.')[1] + "\":")
    for (name, typ) in benchmark.input_relations.items():
        arity = len(typ)
        print("\t" + name + " = Relation(\"" + name + "\", " + str(arity) + ")")
    for (name, typ) in benchmark.output_relations.items():
        arity = len(typ)
        print("\t" + name + " = Relation(\"" + name + "\", " + str(arity) + ")")
    s = [ "Fact(" + ",".join(map(lambda x: str(x), in_r)) + ")" for in_r in benchmark.input_tuples]
    print("\tinput = [" + ",".join(s) + "]")
    
    s = [ "Fact(" + ",".join(map(lambda x: str(x), in_r)) + ")" for in_r in benchmark.output_tuples]
    print("\tpe = [" + ",".join(s) + "]")

    print("\tne = []")

    s = ",".join([ x for x in benchmark.input_relations ])
    print("\tx = EDB([" + s + "], input)")
    
    output_relations = []
    for r in benchmark.output_relations:
        output_relations.append(r)
    s = "\ts = STask(x, [" + ",".join(output_relations) + "], pe, ne, domain = " + str(max_size)
    if benchmark.base is not None:
        s = s + ", base = " + str(benchmark.base)
    if benchmark.chain is not None:
        s = s + ", chain = " + str(benchmark.chain)
    s += ")"
    print(s)

    s = "\tstats = s.synthesize("
    if benchmark.nc is not None:
        s = s + "nc = " + str(benchmark.nc)
    if benchmark.nl is not None:
        s = s + ", nl = " + str(benchmark.nl)
    if benchmark.bound is not None:
        s = s + ", bound = " + str(benchmark.bound)
    s += ")"
    print(s)
elif args.to == "metagol":
    print("#!/usr/local/bin/swipl -c")
    print(":- use_module('../metagol').")
    print("\n%% predicates which can be used in the learning")
    for (relation, args) in benchmark.input_relations.items():
        print("prim(" + relation.lower() + "/" + str(len(args)) + ").")
    print("\n%% first-order background knowledge")
    for in_r in benchmark.input_tuples:
        print(in_r[0].lower() + "(" + ",".join(map(lambda x: str(x), in_r[1:])) + ").")
    print("\n%% learning tasks")
    print("total :-")
    examples = {}
    for out_r in benchmark.output_tuples:
        if out_r[0] not in examples:
            examples[out_r[0]] = []
        examples[out_r[0]].append(out_r[1:])
    for (name, tuples) in examples.items():
        print("\tSubtask_" + name.lower() + " =")
        print("\t[")
        print("\t" + ",\n\t".join(map(lambda t: name.lower() + "(" + ",".join(map(str,t)) + ")", tuples)))
        print("\t]/[],")
    
    s = []
    for name in examples:
        s.append("Subtask_" + name.lower())
    print("learn_seq([" + ",".join(s) + "], Prog),")
    print("pprint(Prog).")
    print("\ngoal :- time(total).")
    print(":- initialization(goal).\n")

    for r in benchmark.rules:
        meta_rule_names = []
        for l in r:
            meta_rule_names.append(l.split('(')[0].upper())
            meta_rule_header = r[0].upper().replace(":", "").replace("(", ",").replace(")", "")
        meta_rule_tail = []
        for l in r[1:]:
            meta_rule_tail.append("[" + l.upper().replace(":", "").replace("(", ",").replace(")", "") + "]")
        meta_rule_tail = ",".join(meta_rule_tail)
        print("metarule([" + ",".join(meta_rule_names) + "], ([" + meta_rule_header + "] :- [" + meta_rule_tail + "])).")
elif args.to == "nlp":
    name = module_name.split('.')[1]
    with open ("neural-lp/" + name + "/entities.txt", 'w') as f:
        for (dom, size) in benchmark.input_domains.items():
            for i in range(0, size):
              f.write(dom + str(i) + "\n")
    with open ("neural-lp/" + name + "/relations.txt", 'w') as f:
        for r in benchmark.input_relations:
            f.write(r + "\n")
        for r in benchmark.output_relations:
            f.write(r + "\n")
    with open ("neural-lp/" + name + "/facts.txt", 'w') as f:
        for r in benchmark.input_tuples:
            dom1 = benchmark.input_relations[r[0]][0]
            dom2 = benchmark.input_relations[r[0]][1]
            f.write(dom1 + str(r[1]) + "\t" + r[0] + "\t" + dom2 + str(r[2]) + "\n")
    train_tuples = benchmark.output_tuples
    test_tuples = original_output
    with open ("neural-lp/" + name + "/train.txt", 'w') as f:
        for r in train_tuples:
            dom1 = benchmark.output_relations[r[0]][0]
            dom2 = benchmark.output_relations[r[0]][1]
            f.write(dom1 + str(r[1]) + "\t" + r[0] + "\t" + dom2 + str(r[2]) + "\n")
    with open ("neural-lp/" + name + "/test.txt", 'w') as f:
        for r in test_tuples:
            dom1 = benchmark.output_relations[r[0]][0]
            dom2 = benchmark.output_relations[r[0]][1]
            f.write(dom1 + str(r[1]) + "\t" + r[0] + "\t" + dom2 + str(r[2]) + "\n")

elif args.to == "difflog":
    correct_name = module_name[module_name.find(".") + 1:]
    print("package qd")
    print("package learner")
    print("import org.scalatest.{FunSuite, Ignore}")
    print("@Ignore")
    print("class Gen%s_%d extends Problem {" % (correct_name, int(args.random * 100)))
    print("\toverride val name = \"%s\"" % correct_name)
    for d in benchmark.input_domains:
        print("\tval %sSet = Range(0, %d).map(i => Atom(i)).toSet" % (d, benchmark.input_domains[d]))
        print("\tval %s = Domain(\"%s\", %sSet)" % (d, d, d))

    tuple_map = {}
    for n in benchmark.input_relations:
        r = benchmark.input_relations[n]
        tuple_map[n] = []
        relation_line = ["\tval %s = Relation(\"%s\", " % (n, n)]
        for x in r:
            relation_line.append(str(x) + ",")
        relation_line[-1] = relation_line[-1][:-1]
        relation_line.append(")")
        print("".join(relation_line))

    for n in benchmark.output_relations:
        r = benchmark.output_relations[n]
        tuple_map[n] = []
        relation_line = ["\tval %s = Relation(\"%s\", " % (n,n)]
        for x in r:
            relation_line.append(str(x) + ",")
        relation_line[-1] = relation_line[-1][:-1]
        relation_line.append(")")
        print("".join(relation_line))


    for r in benchmark.input_tuples + benchmark.output_tuples:
        tuple_map[r[0]].append(tuple(r[1:]))

    for x in tuple_map:
        tuples_line = ["\tval %sTuples = Set(" % x]
        for t in tuple_map[x]:
            if len(t) == 1:
                tuples_line.append(str(t[0]) + ",")
            else:
                tuples_line.append(str(t) + ",")
        tuples_line[-1] = tuples_line[-1][:-1]
        tuples_line.append(").map { case (")
        
        for i in range(len(tuple_map[x][0])):
            tuples_line.append("x%d," % i)
        tuples_line[-1] = tuples_line[-1][:-1]
        tuples_line.append(") => DTuple(")

        for i in range(len(tuple_map[x][0])):
            tuples_line.append("Atom(x%d)," % i)
        tuples_line[-1] = tuples_line[-1][:-1]
        tuples_line.append(") }")


        print ("".join(tuples_line))

    print("\toverride val edb = Config(")
    for r in benchmark.input_relations:
        print("\t\t%s -> (Instance(%s) ++ %sTuples.map(t => t -> One).toMap)," % (r, r, r))
    print("\t)")
    
    print("\toverride val refOut = Config(")
    for r in benchmark.output_relations:
        print("\t\t%s -> (Instance(%s) ++ %sTuples.map(t => t -> One).toMap)," % (r, r, r))
    print("\t)")

    vars = {}
    for r in benchmark.rules:
        for p in r:
            head = p[:p.find("(")]
            p = p[p.find("(") + 1:-1]
            vs = p.split(',')
            for v in vs:
                if v in vars:
                    continue
                if ":" in v:
                    new_name = v.replace(":", "")
                    domain = v[v.find(":") + 1:]
                    vars[v] = (new_name, domain)
                else:
                    for x in benchmark.input_domains:
                        vars[v] = (v, x)
                        break

    for v in vars:
        print("\tval %s = Variable(\"%s\",%s)" % (vars[v][0], vars[v][0], vars[v][1]))


    print "\tval soup = Set("
    for i in range(len(benchmark.rules)):
        if args.weight is None: # TODO: handle reduced soup
            weight = 0.5
        else:
            try:
                weight = benchmark.rule_weights[args.weight][i][1]
            except:
                print("// WARN: not enough rule weights. maybe because of rule-cutoff")
                weight = 0.0
        lines = ["\t\tRule(%d, Value(%f, Token(%d)), " % (i+1,weight,i+1)]
        for x in benchmark.rules[i]:
            new_line = x.replace(':', '')
            lines.append(new_line)
            lines.append(",")
        lines = lines[:-1]
        lines.append("),")
        print "".join(lines)
    print "\t)"
    print "\tval soupProg = Program(\"%sSoup\", soup)" % correct_name
    print "\tval evaluator = SeminaiveEvaluator(soupProg)"
    print "}"

else:
    print("Invalid Argument: " + args.to)
