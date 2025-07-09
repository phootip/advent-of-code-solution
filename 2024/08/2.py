from pprint import pp
from collections import defaultdict
from itertools import combinations, pairwise

map = []
antennas = defaultdict(set)
antinodes = set()
M, N = -1, -1


def parse():
    # f = open("example.txt")
    # f = open("example2.txt")
    f = open("input.txt")
    for l in f:
        map.append(l.strip())

    global M, N
    M, N = len(map[0]), len(map)
    for j in range(N):
        for i in range(M):
            if map[j][i] != ".":
                antennas[map[j][i]].add((i, j))
    return M, N


def inRange(n):
    return 0 <= n[0] < M and 0 <= n[1] < N


def calAnti():
    for k, v in antennas.items():
        for a, b in combinations(v, 2):
            n1, n2 = [-1, -1], [-1, -1]
            if a[0] > b[0]:
                a, b = b, a
            print(a, b)
            dx, dy = (abs(i - j) for i, j in zip(a, b))
            print("diff:", dx, dy)

            print("cal n1...")
            i = 0
            while True:
                n1[0] = a[0] - dx * i
                if a[1] > b[1]:
                    n1[1] = a[1] + dy * i
                else:
                    n1[1] = a[1] - dy * i
                if not inRange(n1):
                    break
                i += 1
                print(n1)
                antinodes.add(tuple(n1))

            print("cal n2...")
            i = 0
            while True:
                n2[0] = b[0] + dx * i
                if a[1] > b[1]:
                    n2[1] = b[1] - dy * i
                else:
                    n2[1] = b[1] + dy * i
                if not inRange(n2):
                    break
                i += 1
                print(n2)
                antinodes.add(tuple(n2))


def main():
    M, N = parse()
    global antinodes
    pp(map)
    pp(antennas)
    calAnti()
    antinodes = [n for n in antinodes if inRange(n)]
    print(len(antinodes))


main()
