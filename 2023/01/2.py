filename = 'input.txt'
# filename = "example2.txt"
f = open(filename, "r")

wordToNum = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
output = 0
for line in f:
    if not line:
        continue
    first, last = None, None
    for i, char in enumerate(line):
        if "0" <= char <= "9":
            if first is None:
                first = char
            last = char
        else:
            for word, num in wordToNum.items():
                if line[i:].startswith(word):
                    if first is None:
                        first = num
                    last = num
    print(first, last)
    output += int(first + last)
print(output)
