import functools

with open("Day 14 - Parabolic Reflector Dish\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]

#Transform to list
for i,line in enumerate(lines):
    lines[i] = list(line)

def move_rocks(lines,rotation):

    changed = False
    #NORTH
    if rotation == 0:
        for j in range(1,len(lines)):

            for i in range(0,len(lines[j])):
                
                if lines[j][i] == 'O' and lines[j-1][i] == '.':
                    lines[j][i] = '.'
                    lines[j-1][i] = 'O'
                    changed = True

    #WEST
    elif rotation == 1:
        for j in range(0,len(lines)):

            for i in range(1,len(lines[j])):
                
                if lines[j][i] == 'O' and lines[j][i-1] == '.':
                    lines[j][i] = '.'
                    lines[j][i-1] = 'O'
                    changed = True

    #SOUTH
    elif rotation == 2:
        for j in range(0,len(lines)-1):

            for i in range(len(lines[j])):
                
                if lines[j][i] == 'O' and lines[j+1][i] == '.':
                    lines[j][i] = '.'
                    lines[j+1][i] = 'O'
                    changed = True

    #EAST
    elif rotation == 3:
        for j in range(0,len(lines)):

            for i in range(0,len(lines[j])-1):
                
                if lines[j][i] == 'O' and lines[j][i+1] == '.':
                    lines[j][i] = '.'
                    lines[j][i+1] = 'O'
                    changed = True

    if changed:
        move_rocks(lines,rotation)

    


def calculate(lines):
    score = 0
    for j in range(0,len(lines)):

        for i in range(len(lines[j])):

            if lines[j][i] == 'O':
                score += len(lines) - j 


    return score


number_of_cycles = 188

#It loops every 14 cycles starting at 176 so 188 cycles are enough
for i in range(number_of_cycles):
    move_rocks(lines,0)
    move_rocks(lines,1)
    move_rocks(lines,2)
    move_rocks(lines,3)

print(calculate(lines))


