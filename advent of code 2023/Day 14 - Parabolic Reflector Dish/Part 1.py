with open("Day 14 - Parabolic Reflector Dish\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]

#Transform to list
for i,line in enumerate(lines):
    lines[i] = list(line)


def move_rocks(lines):
    changed = False
    for j in range(1,len(lines)):

        for i in range(len(lines[j])):
            
            if lines[j][i] == 'O' and lines[j-1][i] == '.':
                lines[j][i] = '.'
                lines[j-1][i] = 'O'
                changed = True

    if changed:
        move_rocks(lines)


def calculate(lines):
    score = 0
    for j in range(0,len(lines)):

        for i in range(len(lines[j])):

            if lines[j][i] == 'O':
                score += len(lines) - j 


    return score



move_rocks(lines)
print(calculate(lines))
