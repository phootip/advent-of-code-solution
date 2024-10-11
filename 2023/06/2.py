from util import parseInput
from pprint import pprint
import re

filename = "input.txt"
# filename = "example.txt"

data = parseInput(filename)
ans = 1
t = ""
d = ""
for race in data:
    t += str(race["t"])
    d += str(race["d"])
ways = 0
t, d = int(t), int(d)
for i in range(1, t // 2 + 1):
    if i * (t - i) > d:
        ways += 1
ways *= 2
if t % 2 == 0:
    if (t // 2) ** 2 > d:
        ways -= 1
# print("result of: ", t, d)
# print(ways)
ans *= ways
# break
print(ans)
