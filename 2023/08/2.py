from util import parseInput
from pprint import pprint
from collections import Counter
from math import lcm
from time import sleep
import re

filename = "input.txt"
# filename = "example3.txt"

inst, data = parseInput(filename)
# for k, v in data.items():
#     print(k, v)
ans = 0
roots = []
for val in data:
    if val[2] == "A":
        roots.append(data[val])
mem = []
for node in roots:
    steps = 0
    start = 0
    loop = 0
    target = ""
    while node.val[2] != "Z" or loop == 0:
        for d in inst:
            if d == "L":
                node = node.l
            else:
                node = node.r
            steps += 1
            if target == node.val:
                loop = steps - start
                break
            if node.val[2] == "Z":
                start = steps
                target = node.val
    # mem.append((start, loop))
    mem.append(start)
    print(steps)
    print(mem)
print(lcm(*mem))
# print(ans)
