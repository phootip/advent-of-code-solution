import re
from pprint import pprint
from collections import defaultdict


def parseInput(filename):
    f = open(filename, "r")
    output = []
    for line in f:
        line = line.strip().split()
        output.append((line[0], int(line[1])))
    return output
