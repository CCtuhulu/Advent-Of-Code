
with open('Day 1 - Not Quite Lisp\input.txt', 'r') as file:
    line = file.readlines()


floor = 0
for chr in line[0]:
    if chr == '(':
        floor += 1

    elif chr == ')':
        floor -= 1

print(floor)