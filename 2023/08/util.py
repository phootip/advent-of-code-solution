import re
from pprint import pprint
from collections import defaultdict


class Node:
    def __init__(self, val, l, r) -> None:
        self.val = val
        self.l = l
        self.r = r

    def __str__(self):
        # return f"val: {self.val}, left: {self.l}, right: {self.r}"
        return f"val: {self.val}, left: {self.l.val}, right: {self.r.val}"


def parseInput(filename):
    f = open(filename, "r")
    ints = f.readline().strip()
    output = {}
    puzzle_input = f.read()
    for data in re.findall(r"(\w+) = \((\w+), (\w+)\)", puzzle_input):
        val, l, r = data
        for node in data:
            if node not in output:
                output[node] = Node(node, None, None)
        output[val].l = output[l]
        output[val].r = output[r]
    return ints, output
