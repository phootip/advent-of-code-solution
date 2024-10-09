from util import parseInput
from itertools import product
import re

filename = "input.txt"
# filename = "example.txt"

data = parseInput(filename)
X, Y = len(data[0]), len(data)

data2 = {}
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


def adjToSpecial(start, end):
    x, y = start
    while x <= end[0]:
        adj = [
            (i, j)
            for i, j in list(product(range(x - 1, x + 2), range(y - 1, y + 2)))
            if (i, j) != (x, y) and 0 <= i < X and 0 <= j < Y
        ]
        for i, j in adj:
            if data[j][i] not in notSpecial:
                return True
        x += 1
    return False


# print(data2)
ans = 0
for p in data2.values():
    if adjToSpecial(p["start"], p["end"]):
        ans += p["value"]
print(ans)
