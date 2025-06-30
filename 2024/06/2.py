from pprint import pp

# f = open("example.txt")
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
original_g = g
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


def hasLoop(p):
    seen2 = []
    data2 = data[:]
    x, y = p
    data2[y] = data2[y][:x] + "#" + data2[y][x + 1 :]

    global g, dir
    while True:
        seen2.append(g)
        new_pos = tuple(a + b for a, b in zip(g, dir))
        if not inRange(new_pos):
            return False
        x, y = new_pos
        if data2[y][x] == "#":
            dir = turnR(dir)
        else:
            g = new_pos
        if len(seen2) > M * N:
            return True
        # print(seen2)


while True:
    output = update()
    if output != -1:
        break
print(output)

output1 = output
output = 0
seen.remove(original_g)
while seen:
    p = seen.pop()
    print(len(seen))
    g, dir = original_g, (0, -1)
    output += 1 if hasLoop(p) else 0

print(output)
