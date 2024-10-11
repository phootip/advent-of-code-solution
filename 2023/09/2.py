from util import parseInput
from pprint import pprint
from collections import Counter
import re

filename = "input.txt"
# filename = "example.txt"

data = parseInput(filename)
ans = 0
for seq in data:
    mem = [seq]
    while not all([x == 0 for x in mem[-1]]):
        last_seq = mem[-1]
        new_seq = [0] * (len(last_seq) - 1)
        for i in range(len(last_seq) - 1):
            new_seq[i] = last_seq[i + 1] - last_seq[i]
        mem.append(new_seq)
    # print(mem)
    mem.pop()
    last_val = 0
    while mem:
        seq = mem.pop()
        last_val = seq[0] - last_val
    print(last_val)
    ans += last_val
print(ans)
