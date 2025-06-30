from collections import defaultdict
import re

f = open("example.txt")
# f = open("input.txt")

rules = defaultdict(set)
queries = []
rule_pattern = r"([0-9]{2})\|([0-9]{2})"
state = 0
for line in f:
    line = line.strip()
    if line == "":
        state = 1
        continue
    if state == 0:
        match = re.search(rule_pattern, line)
        a, b = match.groups()
        a, b = int(a), int(b)
        rules[a].add(b)
    elif state == 1:
        line = line.split(",")
        q = [int(n) for n in line]
        queries.append(q)

# print(rules)
# print(queries)


def process(q):
    seen = set()
    for n in q:
        if seen.intersection(rules[n]):
            return 0
        seen.add(n)
    return q[len(q) // 2]


output = 0
for q in queries:
    output += process(q)
print(output)
