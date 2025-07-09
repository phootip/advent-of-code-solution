from pprint import pp
from collections import defaultdict
from itertools import combinations, pairwise

map = []
antennas = defaultdict(set)
antinodes = set()


def parse():
    # f = open("example.txt")
    f = open("input.txt")
    for l in f:
        map.append(l.strip())

    M, N = len(map[0]), len(map)
    for j in range(N):
        for i in range(M):
            if map[j][i] != ".":
                antennas[map[j][i]].add((i, j))
    return M, N


def calAnti():
    for k, v in antennas.items():
        for a, b in combinations(v, 2):
            n1, n2 = [-1, -1], [-1, -1]
            if a[0] > b[0]:
                a, b = b, a
            print(a, b)
            dx, dy = (abs(i - j) for i, j in zip(a, b))
            print("diff:", dx, dy)
            n1[0] = a[0] - dx
            n2[0] = b[0] + dx
            if a[1] > b[1]:
                n1[1] = a[1] + dy
                n2[1] = b[1] - dy
            else:
                n1[1] = a[1] - dy
                n2[1] = b[1] + dy
            print("antinode:", n1, n2)
            antinodes.add(tuple(n1))
            antinodes.add(tuple(n2))


def main():
    M, N = parse()
    global antinodes
    pp(map)
    pp(antennas)
    calAnti()
    antinodes = [n for n in antinodes if 0 <= n[0] < M and 0 <= n[1] < N]
    print(len(antinodes))


main()
