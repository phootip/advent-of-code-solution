import re

f = open("example.txt")
f = open("input.txt")

pattern = r"\d+"
data = []
for l in f:
    match = re.findall(pattern, l)
    match = list(map(int, match))
    data.append(match)


def check(t, ns, idx):
    if t < 0 or idx >= len(ns):
        return False
    n = ns[idx]
    if idx == len(ns) - 1 and n == t:
        return True
    output = False
    if t % n == 0:
        output = output or check(t // n, ns, idx + 1)
    return output or check(t - n, ns, idx + 1)


output = 0
for q in data:
    target = q[0]
    numbers = q[1:][::-1]
    if check(target, numbers, 0):
        print(target)
        output += target
print("output:", output)
