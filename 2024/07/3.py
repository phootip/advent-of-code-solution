import re
# 226339553043274 too low
# 226340041164107 too low

# f = open("example.txt")
# f = open("input.txt")
f = open("debug1.txt")

pattern = r"\d+"
data = []
for l in f:
    match = re.findall(pattern, l)
    match = list(map(int, match))
    data.append(match)


def check(t, ns, idx):
    print(t, idx)
    if t == 0 and idx == len(ns):
        return True
    if t < 0 or idx >= len(ns):
        return False
    n = ns[idx]
    # if idx == len(ns) - 1 and n == t:
    #     return True
    output = False
    if t % n == 0:
        output = output or check(t // n, ns, idx + 1)
    if t != n and str(t).endswith(str(n)):
        t = int(str(t)[: -len(str(n))])
        output = output or check(t, ns, idx + 1)
    return output or check(t - n, ns, idx + 1)


def check2(t, ns, idx):
    print(t, idx)
    # if t == 0 and idx == len(ns):
    #     return True
    if t < 0 or idx >= len(ns):
        return False
    n = ns[idx]
    if idx == (len(ns) - 1) and n == t:
        return True
    output = False
    if t % n == 0:
        output = output or check2(t // n, ns, idx + 1)
    if t > n and str(t).endswith(str(n)):
        t = int(str(t)[: -len(str(n))])
        output = output or check2(t, ns, idx + 1)
    return output or check2(t - n, ns, idx + 1)


output = 0
mem = set()
mem2 = set()
for q in data:
    target = q[0]
    numbers = q[1:][::-1]
    if check(target, numbers, 0):
        print(target)
        output += target
        mem.add(target)
    else:
        print(f"Nope: {target}")
print("output:", output)

output = 0
for q in data:
    target = q[0]
    numbers = q[1:][::-1]
    if check2(target, numbers, 0):
        # print(target)
        output += target
        mem2.add(target)
    else:
        print(f"Nope: {target}")
print("output:", output)
print(mem.difference(mem2))
