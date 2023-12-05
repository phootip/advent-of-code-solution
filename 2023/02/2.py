from util import parseInput
filename = 'input.txt'
# filename = 'example.txt'

data = parseInput(filename)
ans = 0
for id, turns in data.items():
    print(id,turns)
    upper = {'red': 0, 'green': 0, 'blue': 0}
    for turn in turns:
        for color in ['red','green','blue']:
            upper[color] = max(upper[color], turn[color])
    ans += upper['red']*upper['green']*upper['blue']
print(ans)
