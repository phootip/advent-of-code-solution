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

for i, n in enumerate(mem):
    while mem[-1] == ".":
        mem.pop()
    if i >= len(mem):
        break
    if n == ".":
        mem[i] = mem.pop()
print(mem)

output = 0
for i, n in enumerate(mem):
    output += i * n
print(output)
