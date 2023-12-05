def parseInput(filename):
    f = open(filename, 'r')
    output = {}
    for line in f:
        if not line: continue
        line = line.strip().split(': ')
        id = int(line[0][5:])
        output[id] = []
        turns = line[1].split('; ')
        turns = list(map(lambda x: x.split(', '), turns))
        for turn in turns:
            t = {'red':0,'green':0,'blue':0}
            for cube in turn:
                n, color = cube.split(' ')
                t[color] = int(n)
            output[id].append(t)
    f.close()
    return output
