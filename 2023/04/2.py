from util import parseInput
import re

filename = "input.txt"
# filename = "example.txt"

data = parseInput(filename)
score = {k: 1 for k in data.keys()}
print(score)
for card, values in data.items():
    a, b = values["a"], values["b"]
    b = set(b)
    winning = sum([1 if n in b else 0 for n in a])
    if winning == 0:
        continue
    # print(card, winning)
    for i in range(card + 1, card + winning + 1):
        score[i] += score[card]
print(score)
print(sum(score.values()))
