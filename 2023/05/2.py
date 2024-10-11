from util import parseInput
from pprint import pprint
import re

filename = "input.txt"
# filename = "input2.txt"
# filename = "example.txt"

seeds, data = parseInput(filename)
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append(
        {
            "node": "seed",
            "start": seeds[i],
            "end": seeds[i] + seeds[i + 1] - 1,
            "path": [seeds[i]],
        }
    )
# print(seed_ranges)
# print()
# pprint(data)


def getNextRange(seed_range):
    node, path = seed_range["node"], seed_range["path"]
    start, end = seed_range["start"], seed_range["end"]
    mapping = data[node]
    des = mapping[0]["des"]
    l, r = 0, len(mapping) - 1
    result = 0
    while l <= r:
        m = (l + r) // 2
        if mapping[m]["src_start"] < start:
            result = max(result, m)
            l = m + 1
        elif mapping[m]["src_start"] > start:
            r = m - 1
        else:
            result = m
            break
    l = result
    # print(mapping)
    # print(mapping[l])
    src_start, des_start = mapping[l]["src_start"], mapping[l]["des_start"]
    src_end = mapping[l]["src_end"]
    diff = des_start - src_start
    if start < src_start and src_end < end:
        print("Error phoo")
        exit(0)
    if end < src_start or src_end < start:
        seed_ranges.append(
            {"node": des, "start": start, "end": end, "path": path[:] + [start]}
        )
    elif src_start <= start <= end <= src_end:
        seed_ranges.append(
            {
                "node": des,
                "start": start + diff,
                "end": end + diff,
                "path": path[:] + [start],
            }
        )
    elif src_start <= start <= src_end and src_end < end:
        seed_ranges.append(
            {
                "node": des,
                "start": start + diff,
                "end": src_end + diff,
                "path": path[:] + [start],
            }
        )
        seed_ranges.append(
            {"node": node, "start": src_end + 1, "end": end, "path": path[:]}
        )
    elif src_start <= end <= src_end and start < src_start:
        seed_ranges.append(
            {
                "node": des,
                "start": src_start + diff,
                "end": end + diff,
                "path": path[:] + [start],
            }
        )
        seed_ranges.append(
            {"node": node, "start": start, "end": src_start - 1, "path": path[:]}
        )
    else:
        print("Error phootip!")
        exit(1)
    # return des, start + diff


ans = float("inf")
while seed_ranges:
    seed_range = seed_ranges.pop()
    # print(seed_range)
    if seed_range["node"] == "location":
        print(f'location: {seed_range["start"]}')
        ans = min(ans, seed_range["start"])
    else:
        getNextRange(seed_range)
    # print()
print(ans)
