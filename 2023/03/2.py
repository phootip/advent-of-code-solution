from util import parseInput
from itertools import product
from collections import defaultdict
from pprint import pprint
import re

filename = "input.txt"
# filename = "example.txt"

data = parseInput(filename)
X, Y = len(data[0]), len(data)

data2 = {}
data_asterisk = defaultdict(list)
for y in range(Y):
    n = ""
    path = []
    for x in range(X):
        c = data[y][x]
        if re.search("[0-9]", c):
            path.append((x, y))
            n += c
        else:
            if n != "":
                p = path[0]
                data2[p] = {"value": int(n), "start": path[0], "end": path[-1]}
            n = ""
            path = []
    if n != "":
        p = path[0]
        data2[p] = {"value": int(n), "start": path[0], "end": path[-1]}

notSpecial = [str(i) for i in range(0, 10)] + ["."]


def adjToAsterisk(point):
    value, start, end = point["value"], point["start"], point["end"]
    x, y = start
    visited = set()
    while x <= end[0]:
        adj = [
            (i, j)
            for i, j in list(product(range(x - 1, x + 2), range(y - 1, y + 2)))
            if (i, j) != (x, y) and 0 <= i < X and 0 <= j < Y and (i, j) not in visited
        ]
        visited.update(adj)
        for i, j in adj:
            if data[j][i] == "*":
                data_asterisk[(i, j)].append(value)
        # print(adj)
        # print(visited)
        # print(data_asterisk)
        # print()
        x += 1
    return False


# print(data2)
ans = 0
for p in data2.values():
    adjToAsterisk(p)
for arr in data_asterisk.values():
    if len(arr) != 2:
        continue
    ans += arr[0] * arr[1]
print(ans)
