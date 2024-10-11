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
l = 1
while l * (t - l) <= d:
    l += 1
ans = t - 2 * l + 1
print(ans)
