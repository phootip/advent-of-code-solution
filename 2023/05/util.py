import re
from pprint import pprint
from collections import defaultdict


def parseInput(filename):
    f = open(filename, "r")
    output = defaultdict(list)
    roots = []
    src, des = "", ""
    for i, line in enumerate(f):
        line = line.strip()
        if not line:
            continue
        line = line.split(" ")
        if line[0] == "seeds:":
            for s in line[1:]:
                roots.append(int(s))
        elif line[1] == "map:":
            src, des = line[0].split("-to-")
        else:
            output[src].append(
                {
                    "des_start": int(line[0]),
                    "src_start": int(line[1]),
                    "src_end": int(line[1]) + int(line[2]) - 1,
                    "range": int(line[2]),
                    "des": des,
                    "diff": int(line[0]) - int(line[1]),
                }
            )
    for k in output:
        output[k] = sorted(output[k], key=lambda x: x["src_start"])
    for k, v in output.items():
        for i in range(len(v) - 1):
            if v[i]["src_end"] + 1 != v[i + 1]["src_start"]:
                v.append(
                    {
                        "des_start": v[i]["src_end"] + 1,
                        "src_start": v[i]["src_end"] + 1,
                        "src_end": v[i + 1]["src_start"] - 1,
                        "range": v[i + 1]["src_start"] - 1 - v[i]["src_end"] - 1,
                        "des": des,
                        "diff": 0,
                    }
                )
    for k in output:
        output[k] = sorted(output[k], key=lambda x: x["src_start"])
    f.close()
    return roots, output
