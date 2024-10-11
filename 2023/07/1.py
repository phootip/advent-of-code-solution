from util import parseInput
from pprint import pprint
from collections import Counter
import re

filename = "input.txt"
# filename = "example.txt"

data = parseInput(filename)
print(data)

power_mapping = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def camelCard(a):
    mem = []
    card = a[0]
    c = sorted(Counter(card).items(), key=lambda x: -x[1])
    t = 0
    if c[0][1] == 5:
        t = 7
    elif c[0][1] == 4:
        t = 6
    elif c[0][1] == 3 and c[1][1] == 2:
        t = 5
    elif c[0][1] == 3:
        t = 4
    elif c[0][1] == 2 and c[1][1] == 2:
        t = 3
    elif c[0][1] == 2:
        t = 2
    elif c[0][1] == 1:
        t = 1
    else:
        print("Unidentified type")
        exit(0)
    mem.append(t)
    for i in card:
        if i in power_mapping:
            mem.append(power_mapping[i])
        else:
            mem.append(int(i))
    return tuple(mem)


ans = 0
data = sorted(data, key=camelCard)
for i, (h, bid) in enumerate(data):
    ans += bid * (i + 1)

print(ans)
