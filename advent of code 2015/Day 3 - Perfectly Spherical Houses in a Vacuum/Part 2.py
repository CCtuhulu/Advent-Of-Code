
with open('Day 3 - Perfectly Spherical Houses in a Vacuum\input.txt', 'r') as file:
    lines = file.readlines()

posS = (0,0)
posR = (0,0) 
houses_visited = []

for i, chr in enumerate(lines[0]):


    if i%2 == 0:
        pos = posS
    else:
        pos = posR

    houses_visited.append(pos)

    if chr == '>':
        pos = (pos[0]+1, pos[1])
    elif chr == '<':
        pos = (pos[0]-1, pos[1])
    elif chr == '^':
        pos = (pos[0], pos[1]+1)
    elif chr == 'v':
        pos = (pos[0], pos[1]-1)

    if i%2 == 0:
        posS = pos
    else:
        posR = pos


unique_houses = len(set(houses_visited))
print(unique_houses)