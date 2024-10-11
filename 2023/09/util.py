import re
from pprint import pprint
from collections import defaultdict


def parseInput(filename):
    f = open(filename, "r")
    output = []
    for line in f:
        line = [int(n) for n in line.strip().split()]
        output.append(line)
    return output
