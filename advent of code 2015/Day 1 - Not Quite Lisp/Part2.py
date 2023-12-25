
with open('Day 1 - Not Quite Lisp\input.txt', 'r') as file:
    line = file.readlines()


floor = 0
result = 0
for i, chr in enumerate(line[0]):
    if chr == '(':
        floor += 1

    elif chr == ')':
        floor -= 1

    if floor == -1:
        result = i+1
        break

print(result)