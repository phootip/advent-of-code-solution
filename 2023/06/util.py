import re
from pprint import pprint
from collections import defaultdict


def parseInput(filename):
    f = open(filename, "r")
    output = []
    times = f.readline().strip().split()[1:]
    distances = f.readline().strip().split()[1:]
    for i in range(len(times)):
        output.append({"t": int(times[i]), "d": int(distances[i])})
    return output
