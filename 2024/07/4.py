import re
# 226339553043274 too low
# 226340041164107 too low
# 227615740238334

# f = open("example.txt")
f = open("input.txt")
# f = open("debug1.txt")

pattern = r"\d+"
data = []
for l in f:
    match = re.findall(pattern, l)
    match = list(map(int, match))
    data.append(match)


def check(t, ns, idx, acc):
    # print(t, 1, acc)
    if idx == len(ns) and t == acc:
        return True
    if idx >= len(ns):
        return False
    n = ns[idx]
    output = False
    output = output or check(t, ns, idx + 1, acc + n)
    output = output or check(t, ns, idx + 1, acc * n)
    output = output or check(t, ns, idx + 1, int(str(acc) + str(n)))
    return output


output = 0
mem = set()
for q in data:
    target = q[0]
    numbers = q[1:]
    if check(target, numbers, 0, 0):
        print(target)
        output += target
        mem.add(target)
    else:
        print(f"Nope: {target}")
print("output:", output)
