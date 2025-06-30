f = open("example.txt")
f = open("input.txt")

data = []
for l in f:
    l = l.strip()
    data.append(l)

M, N = len(data[0]), len(data)
dir = (0, -1)
g = (-1, -1)
seen = set()
for y in range(N):
    for x in range(M):
        if data[y][x] == "^":
            g = (x, y)
print(g)


def inRange(pos):
    x, y = pos
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    return True


def get(pos):
    x, y = pos
    return data[y][x]


def turnR(dir):
    return -dir[1], dir[0]


def update():
    global g, dir
    seen.add(g)
    new_pos = tuple(a + b for a, b in zip(g, dir))
    if not inRange(new_pos):
        return len(seen)
    if get(new_pos) == "#":
        new_pos = g
        dir = turnR(dir)
    else:
        g = new_pos
    return -1


while True:
    output = update()
    if output != -1:
        break
print(output)
