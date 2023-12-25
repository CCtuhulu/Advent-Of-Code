import sys

sys.setrecursionlimit(50000)

with open("Day 16 - The Floor Will Be Lava\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]

rows = len(lines)
columns = len(lines[0])
for i,line in enumerate(lines):
    lines[i] = list(line)


#directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
start_position = (-1,0)

visited = []

energy_map = [['.' for _ in range(columns)] for _ in range(rows)]

def move(position,direction):
    if direction == UP:

        if position[1] == 0:
            return 0
        

        new_position = (position[0], position[1]-1)
        if (new_position[0],new_position[1],direction) in visited:
            return 0
        
        else:
            visited.append((new_position[0],new_position[1],direction))
            energy_map[new_position[1]][new_position[0]] = '#'
            tile = lines[new_position[1]][new_position[0]]
            
            if tile == '/':
                move(new_position, RIGHT)

            elif tile == '\\':
                move(new_position, LEFT)

            elif tile == '|':
                move(new_position, UP)

            elif tile == '-':
                move(new_position, RIGHT)
                move(new_position, LEFT)
            
            elif tile == '.':
                move(new_position, UP)

    elif direction == RIGHT:

        if position[0] == columns-1:
            return 0
        
        new_position = (position[0]+1, position[1])

        if (new_position[0],new_position[1],direction) in visited:
            return 0
        
        else:
            visited.append((new_position[0],new_position[1],direction))
            energy_map[new_position[1]][new_position[0]] = '#'
            tile = lines[new_position[1]][new_position[0]]
            
            if tile == '/':
                move(new_position, UP)

            elif tile == '\\':
                move(new_position, DOWN)

            elif tile == '|':
                move(new_position, UP)
                move(new_position, DOWN)

            elif tile == '-':
                move(new_position, RIGHT)
            
            elif tile == '.':
                move(new_position, RIGHT)

    elif direction == DOWN:
        if position[1] == rows-1:
            return 0
        
        new_position = (position[0], position[1]+1)

        if (new_position[0],new_position[1],direction) in visited:
            return 0
        
        else:
            visited.append((new_position[0],new_position[1],direction))
            energy_map[new_position[1]][new_position[0]] = '#'
            tile = lines[new_position[1]][new_position[0]]
            
            if tile == '/':
                move(new_position, LEFT)

            elif tile == '\\':
                move(new_position, RIGHT)

            elif tile == '|':
                move(new_position, DOWN)

            elif tile == '-':
                move(new_position, RIGHT)
                move(new_position, LEFT)
            
            elif tile == '.':
                move(new_position, DOWN)

    elif direction == LEFT:

        if position[0] == 0:
            return 0
        
        new_position = (position[0]-1, position[1])

        if (new_position[0],new_position[1],direction) in visited:
            return 0
        
        else:
            visited.append((new_position[0],new_position[1],direction))
            energy_map[new_position[1]][new_position[0]] = '#'
            tile = lines[new_position[1]][new_position[0]]
            
            if tile == '/':
                move(new_position, DOWN)

            elif tile == '\\':
                move(new_position, UP)

            elif tile == '|':
                move(new_position, UP)
                move(new_position, DOWN)

            elif tile == '-':
                move(new_position, LEFT)
            
            elif tile == '.':
                move(new_position, LEFT)

move(start_position, RIGHT)


total = 0

for row in energy_map:
    total += row.count('#')

print(total)

