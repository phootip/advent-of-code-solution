from util import parseInput
import re

filename = "input.txt"
# filename = "example.txt"

data = parseInput(filename)
ans = 0
for card, values in data.items():
    a, b = values["a"], values["b"]
    b = set(b)
    winning = sum([1 if n in b else 0 for n in a])
    if winning == 0:
        continue
    point = 2 ** (winning - 1)
    ans += point
    print(card, point)
print(ans)
