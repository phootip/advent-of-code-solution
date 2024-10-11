from util import parseInput
from pprint import pprint
from collections import Counter
import re

filename = "input.txt"
# filename = "example.txt"
# filename = "example2.txt"

inst, data = parseInput(filename)
# for k, v in data.items():
#     print(k, v)
ans = 0
node = data["AAA"]
while node.val != "ZZZ":
    for d in inst:
        if d == "L":
            node = node.l
        else:
            node = node.r
        ans += 1
        if node.val == "ZZZ":
            break
print(ans)
