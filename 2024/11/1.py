class Solver:
    def __init__(self) -> None:
        self.data = []

    def parseFile(self, filename):
        f = open(filename)
        for l in f:
            self.data = list(map(int, l.strip().split()))
        print(self.data)

    def update(self):
        data2 = []
        for n in self.data:
            if n == 0:
                data2.append(1)
            elif len(str(n)) % 2 == 0:
                s = str(n)
                l = len(s)
                data2.append(int(s[: l // 2]))
                data2.append(int(s[l // 2 :]))
            else:
                data2.append(n * 2024)
        self.data = data2

    def solve(self, filename):
        self.parseFile(filename)
        for i in range(25):
            self.update()
            # print(self.data)
        return len(self.data)

    def solve2(self, filename):
        self.parseFile(filename)
        for i in range(75):
            self.update()
            print(i, ":", len(self.data))
        return len(self.data)


if __name__ == "__main__":
    solver = Solver()
    print("answer:", solver.solve("example1.txt"))
    print("answer:", solver.solve("input.txt"))
