# f = open("example.txt")
f = open("input.txt")

mem = []
for l in f:
    l = l.strip()
    state = "file"
    i = 0
    while i < len(l):
        id = i // 2
        n = int(l[i])
        if state == "file":
            mem += [id] * n
            state = "free"
        elif state == "free":
            mem += ["."] * n
            state = "file"
        i += 1
print(mem)
mem2 = []
cur = 1
for i, n in enumerate(mem):
    if i == 0:
        continue
    if n == mem[i - 1]:
        cur += 1
    else:
        mem2.append((mem[i - 1], cur))
        cur = 1
mem2.append((mem[i], cur))
mem = mem2
cur_id = mem[-1][0]
print(mem)
print(cur_id)
idx = len(mem) - 1

while idx > 0:
    while idx > 0 and mem[idx][0] != cur_id:
        idx -= 1
    id, size = mem[idx]
    for i, (id2, size2) in enumerate(mem):
        if id2 == "." and size2 >= size:
            mem[idx] = (".", size)
            new_size = size2 - size
            if new_size != 0:
                mem[i] = (".", new_size)
            else:
                mem.pop(i)
            mem.insert(i, (id, size))
            break
        elif id2 == id:
            break
    cur_id -= 1
#     print(mem)
#     print(cur_id)
# print(mem)

mem2 = []
for val, size in mem:
    mem2 += [val] * size
mem = mem2
print(mem)


# print(mem)
#
output = 0
for i, n in enumerate(mem):
    if n == ".":
        continue
    output += i * n
print(output)
