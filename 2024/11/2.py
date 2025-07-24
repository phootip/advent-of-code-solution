from functools import cache


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
                # data2.append(n << 11)
        self.data = data2

    @cache
    def expand(self, n, b):
        if b == 0:
            return 1
        if n == 0:
            return self.expand(1, b - 1)
        elif len(str(n)) % 2 == 0:
            s = str(n)
            l = len(s)
            return self.expand(int(s[: l // 2]), b - 1) + self.expand(
                int(s[l // 2 :]), b - 1
            )
        else:
            return self.expand(n * 2024, b - 1)

    def solve(self, filename):
        self.parseFile(filename)
        # print(self.data)
        # for i in range(6):
        #     self.update()
        #     print(self.data)
        # return len(self.data)

        output = 0
        for n in self.data:
            output += self.expand(n, 75)
        return output


if __name__ == "__main__":
    solver = Solver()
    # print("answer:", solver.solve("example1.txt"))
    print("answer:", solver.solve("input.txt"))
