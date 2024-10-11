from util import parseInput
from pprint import pprint
import re

filename = "input.txt"
# filename = "example.txt"

seeds, data = parseInput(filename)
# pprint(data)


def getNextNum(node, num):
    mapping = data[node]
    des = mapping[0]["des"]
    l, r = 0, len(mapping) - 1
    result = 0
    while l <= r:
        m = (l + r) // 2
        if mapping[m]["src_start"] < num:
            l = m + 1
            result = max(result, m)
        elif mapping[m]["src_start"] > num:
            r = m - 1
        else:
            result = m
            break
    l = result
    # print(mapping)
    # print(mapping[l])

    src_start, des_start = mapping[l]["src_start"], mapping[l]["des_start"]
    src_end = src_start + mapping[l]["range"]
    if not (src_start <= num <= src_end):
        return des, num
    return des, num + (des_start - src_start)


ans = float("inf")
for seed in seeds:
    node = "seed"
    num = seed
    print(node, num)
    while node != "location":
        node, num = getNextNum(node, num)
        # print(node, num)
    print(node, num)
    ans = min(ans, num)
print(ans)
