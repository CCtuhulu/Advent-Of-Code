
with open('Day 3 - Perfectly Spherical Houses in a Vacuum\input.txt', 'r') as file:
    lines = file.readlines()

pos = (0,0)

houses_visited = []

for chr in lines[0]:
    houses_visited.append(pos)
    if chr == '>':
        pos = (pos[0]+1, pos[1])
    elif chr == '<':
        pos = (pos[0]-1, pos[1])
    elif chr == '^':
        pos = (pos[0], pos[1]+1)
    elif chr == 'v':
        pos = (pos[0], pos[1]-1)




unique_houses = len(set(houses_visited))
print(unique_houses)