from util import parseInput
filename = 'input.txt'
# filename = 'example.txt'

def checkPossible(turns,limit):
    for turn in turns:
        for color, n in limit.items():
            if turn[color] > n:
                return False
    return True
    
data = parseInput(filename)
limit = {'red': 12, 'green': 13, 'blue': 14}
ans = 0

for id, turns in data.items():
    if checkPossible(turns,limit):
        ans += id
        print(id)

print(ans)
