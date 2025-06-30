from pprint import pp


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
    # count right
    output = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            output += checkXmas(x, y, dx, dy)
    return output


def checkXmas(x, y, dx, dy):
    for i in range(0, 4):
        if x < 0 or y < 0 or x >= M or y >= N:
            return False
        if data[y][x] != target[i]:
            return False
        x, y = x + dx, y + dy
    return True


# pp(data)
# pp(checkXmas(8, 0, 1, 0))
# pp(checkXmas(2, 0, 1, 1))
# pp(count(5, 0))
output = 0
for j in range(N):
    for i in range(M):
        output += count(i, j)
print(output)
