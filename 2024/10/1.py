from pprint import pp
from itertools import pairwise


lvl = ""


class Solver:
    def __init__(self):
        self.seen = set()
        return

    def clean(self):
        self.seen = set()
        self.M = None
        self.N = None

    def parseFile(self, filename):
        self.clean()
        f = open(filename)
        data = []
        for l in f:
            l = list(map(lambda x: int(x) if x != "." else ".", list(l.strip())))
            data.append(l)
        M, N = len(data[0]), len(data)
        self.M, self.N = M, N
        return data

    def countTrail(self, x, y):
        if data[y][x] == 9:
            return 1
        adj = self.getAdj(x, y)
        output = 0
        for n in adj:
            output += self.countTrail(*n)
        return output

    def getAdj(self, x, y):
        adj = []
        for i, j in pairwise([0, 1, 0, -1, 0]):
            x2, y2 = x + i, y + j
            if (not 0 <= x2 <= self.M - 1) or (not 0 <= y2 <= self.N - 1):
                continue
            if (x2, y2) in self.seen:
                continue
            if data[y2][x2] == ".":
                continue
            if data[y2][x2] - data[y][x] != 1:
                continue
            self.seen.add((x2, y2))
            adj.append((x2, y2))
        return adj

    def solve(self, data):
        print("calculating....")
        output = 0
        for j in range(self.N):
            for i in range(self.M):
                self.seen = set()
                if data[j][i] == 0:
                    output += self.countTrail(i, j)
        return output


if __name__ == "__main__":
    solver = Solver()
    data = solver.parseFile("example1-2.txt")
    print(solver.solve(data))

    data = solver.parseFile("example.txt")
    print(solver.solve(data))

    data = solver.parseFile("input.txt")
    print(solver.solve(data))
