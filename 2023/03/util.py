def parseInput(filename):
    f = open(filename, "r")
    output = {}
    output = [list(line.strip()) for line in f]
    f.close()
    return output
