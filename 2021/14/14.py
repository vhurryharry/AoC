from collections import Counter
import numpy as np
import re

with open('14.in') as infile:
    input = infile.read()

sections = input.split('\n\n')

polymer = sections[0]

rules = np.array(
    list(map(lambda x: x.split(' -> '), sections[1].splitlines())))


def initial_process(polymer, rules):
    rules_count = np.zeros((len(rules), 3), dtype=object)
    rules_count[:, :-1] = rules

    for rule in rules_count:
        indices = [m.start()
                   for m in re.finditer('(?=%s)' % (rule[0]), polymer)]
        rule[2] = len(indices)

    return rules_count


def update_rule(rules, pattern, count):
    indices = np.where(rules == pattern)
    if(len(indices[0]) == 1):
        rules[indices[0][0]][2] += count

    return rules


def process_step(rules):
    new_rules = np.copy(rules)
    new_rules[:, 2] = 0

    for rule in rules:
        new_rules = update_rule(new_rules, rule[0][0] + rule[1], rule[2])
        new_rules = update_rule(new_rules, rule[1] + rule[0][1], rule[2])

    return new_rules


rules = initial_process(polymer, rules)

for i in range(40):
    rules = process_step(rules)

counts = {}
for rule in rules:
    if rule[0][0] in counts.keys():
        counts[rule[0][0]] += rule[2]
    else:
        counts[rule[0][0]] = rule[2]

    if rule[0][1] in counts.keys():
        counts[rule[0][1]] += rule[2]
    else:
        counts[rule[0][1]] = rule[2]

counts[polymer[0]] += 1
counts[polymer[-1]] += 1


result = int((counts[max(counts, key=counts.get)] -
             counts[min(counts, key=counts.get)]) / 2)
print(result)
