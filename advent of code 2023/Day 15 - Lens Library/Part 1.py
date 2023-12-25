with open("Day 15 - Lens Library\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]


instructions = lines[0].split(',')

def hash(instruct):

    result = 0
    for chr in instruct:
        result += ord(chr)
        result *= 17
        result %= 256

    return result

total = 0
for instruct in instructions:
    total += hash(instruct)

print(total)