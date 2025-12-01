from pprint import pp
from itertools import pairwise


# f = open("example.txt")
# f = open("example2.txt")
f = open("input.txt")
data = []
for line in f:
    line = line.strip()
    data.append(line)
M, N = len(data[0]), len(data)
target = "XMAS"


def count(x, y):
    if data[y][x] != "A":
        return 0
    output = 0
    print("check MAS")
    for dx, dy in pairwise([1, 0, -1, 0, 1]):
        output += checkXmas2(x, y, dx, dy)
    return output


def checkXmas2(x, y, dx, dy):
    print(x, y, dx, dy)
    # checkM
    if dx == 0:
        mPoint = [(x + 1, y + dy), (x - 1, y + dy)]
        sPoint = [(x + 1, y - dy), (x - 1, y - dy)]
    else:
        mPoint = [(x + dx, y + 1), (x + dx, y - 1)]
        sPoint = [(x - dx, y + 1), (x - dx, y - 1)]
    print("m:", mPoint)
    print("s:", sPoint)
    if all([data[y][x] == "M" for x, y in mPoint]) and all(
        [data[y][x] == "S" for x, y in sPoint]
    ):
        return True
    return False


# pp(data)
# pp(checkXmas(8, 0, 1, 0))
# pp(checkXmas(2, 0, 1, 1))
# pp(count(2, 1))

output = 0
for j in range(1, N - 1):
    for i in range(1, M - 1):
        output += count(i, j)
print(output)
