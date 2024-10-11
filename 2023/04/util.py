import re
from pprint import pprint


def parseInput(filename):
    f = open(filename, "r")
    output = {}
    for line in f:
        splited_line = line.split()[1:]
        splited_line[0] = splited_line[0][:-1]
        splited_line = [int(i) if i != "|" else "|" for i in splited_line]
        card = splited_line.pop(0)
        output[card] = {"a": [], "b": []}
        target = "a"
        for n in splited_line:
            if n == "|":
                target = "b"
            else:
                output[card][target].append(n)
    f.close()
    return output
