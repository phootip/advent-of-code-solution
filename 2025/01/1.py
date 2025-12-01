from pprint import pp


# f = open("example.txt")
f = open("input.txt")

mem = []


def parse_input(f):
    for l in f:
        l = l.strip()
        mem.append((l[0], int(l[1:])))


def part1():
    output = 0
    dial = 50
    for d, v in mem:
        v %= 100
        if d == "L":
            v = -v
        dial += v
        print(f"{dial=}")
        if dial < 0:
            dial += 100
        elif dial > 100:
            dial -= 100
        elif dial == 0 or dial == 100:
            output += 1
            dial = 0
    return output


def part2():
    output = 0
    dial = 50
    for d, v in mem:
        start = dial
        print(d, v)
        output += v // 100
        v %= 100
        if d == "L":
            v = -v
        dial += v
        print(f"{dial=}")
        if dial < 0:
            dial += 100
            if start != 0:
                output += 1
        elif dial > 100:
            dial -= 100
            if start != 0:
                output += 1
        elif dial == 0 or dial == 100:
            output += 1
            dial = 0
        print(f"{dial=}")
        print(f"{output=}")
    return output


if __name__ == "__main__":
    parse_input(f)
    # print(part1())
    print(part2())
