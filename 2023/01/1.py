filename = 'input.txt'
# filename = 'example.txt'
f = open(filename, 'r')

output = 0
for line in f:
    if not line: continue
    first, last = None, None
    for char in line:
        if '0' <= char <= '9':
            if first is None:
                first = char
            last = char
    output += int(first + last)
print(output)
